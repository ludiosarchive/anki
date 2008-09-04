from time import time
from anki import DeckStorage as ds
print "open deck.."
t = time()
d = ds.Deck("tango.anki", rebuild=False)
print "opened in", time() - t
print "rebuild (new)..",
t = time()
d.rebuildQueue()
print time() - t

import cgi


# timing

for i in range(3):
    t3 = time()
    print "getIds..",
    t = time()
    #raw_input()
    card = d.getCard(orm=False)
    #print card.question.encode("utf-8")
    print time() - t
    t = time()
    print "ans..",
    d.answerCard(card, 1)
    print time() - t; t = time()
    #print "stats.."
    s = d.getStats()

    #print "counts", d.counts()
    #print d.failedCount(
    #print time() - t
    #print "stats", s['failed'], s['successive'], s['new']
    #print "total stats", time() - t
    print "total all", time() - t3

#failhere

# syncing

from anki.sync import SyncClient, HttpSyncServerProxy

proxy = HttpSyncServerProxy("resolve", "abc123")
proxy.connect("ankimini")

if not proxy.hasDeck(d.syncName):
    raise "invalid deck"

print "done connect", time() - t; t = time()

# need to do anything?
proxy.deckName = d.syncName
if d.modified == proxy.modified():
    print "nothing to do"
else:
    print "nothing checked", time() - t; t = time()
    client = SyncClient(d)
    client.setServer(proxy)
    client.sync()
    print "synced", time() - t; t = time()


fail

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

currentCard = None

class Handler(BaseHTTPRequestHandler):

    _top = """
<html>
<head>
<meta name="viewport" content="user-scalable=yes, width=device-width,
    maximum-scale=0.6667" />
<style>
input.button
{ font-size: 12px; width: 85px; height: 50px; padding: 5px;}
</style>
</head>
<body>
"""

    _bottom = """
</form>
</body>
</html>"""

    def do_GET(self):
        t = time()
        global currentCard
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # cgi parms
        try:
            (path, qs) = self.path.split("?")
        except ValueError:
            qs = ""
        query = cgi.parse_qs(qs)
        for k in query:
            query[k] = query[k][0]
        q = query.get("q", None)
        mod = query.get("mod", None)

        buffer = ""

        if self.path.startswith("/question"):
            # possibly answer old card
            if (q is not None and
                currentCard and mod == str(int(currentCard.modified))):
                d.answerCard(currentCard, int(q))
                print "card answered with", q
            # get new card
            c = d.getCard(orm=False)
            stats = self.getStats(d)
            currentCard = c

            buffer += (self._top + ("""
%(stats)s<br>
<h1>%(question)s</h1>
<form action="/answer" method="get">
<input type="submit" class="button" value="Answer">
""" % {
    "question": c.question.encode("utf-8"),
    "stats": stats,
    }))
            buffer += (self._bottom)
        elif self.path.startswith("/answer"):
            if not currentCard:
                currentCard = d.getCard(orm=False)
            c = currentCard
            stats = self.getStats(d)
            buffer += (self._top + """
%(stats)s<br>
<h1>%(question)s<p>%(answer)s</h1>
<form action="/question" method="get">
<input type="hidden" name="mod" value="%(mod)d">
""" % {
    "question": c.question.encode("utf-8"),
    "answer": c.answer.encode("utf-8"),
    "mod": c.modified,
    "stats": stats,
    })
            for i in range(5):
                buffer += ("""
<input type="submit" class="button" name="q" value="%d"/>
""" % i)
            buffer += (self._bottom)
        else:
            buffer += ("invalid request")
        self.wfile.write(buffer + "\n")
        print "service time", time() - t

    def getStats(self, deck):
        s = deck.getStats()
        stats = (("Today: %(dYesTotal)d/%(dTotal)d "
                 "(%(dYesTotal%)3.1f%%) "
                 "Avg: %(dMatureYes%)3.1f%%.<br>Rem: "
                 "%(failed)d+%(successive)d+%(new)d ETA: %(timeLeft)s") % s).encode("utf-8")
        return stats

def run(server_class=HTTPServer,
        handler_class=Handler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

