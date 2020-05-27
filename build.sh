#!/bin/bash

declare -a WEEKS
WEEKS=(1 2 3)

source venv/bin/activate
python3 assets/scripts/navbar.py
echo "Finished assembling navbar"
python3 assets/scripts/announcements.py ${WEEKS[*]}
echo "Finished building index.html"
deactivate
