#!/bin/bash

cd ~/anki
echo "syncing updates..."
rsync -av reflex:Lib/code/libanki --exclude .hg --exclude build --exclude dist --delete .
rsync -av reflex:Lib/code/ankiqt --exclude .hg --exclude build --exclude dist  --delete .
echo "updating kakasi..."
mkdir -p kakasi
cp -Rvf /usr/local/bin/kakasi kakasi
cp -Rvf /usr/local/share/kakasi/kanwadict kakasi
cp -Rvf /usr/local/share/kakasi/itaijidict kakasi
echo "adding image formats..."
cp -Rvf imageformats ankiqt
echo "building..."
PYTHONPATH=ankiqt python ankiqt/mac/setup.py bdist_dmg

