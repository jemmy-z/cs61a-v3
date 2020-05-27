#!/bin/bash

if [ "$1" == "clean" ]
then
    rm temp/*
    echo "Removed all temp files"
    exit
fi

declare -a WEEKS
declare -a ANNOUNCEMENT_FILES
declare -a NAVBAR_FILES

SEMESTER="Fall 2020"
WEEKS=(1 2 3)
NAVBAR_FILES=("index.html" "about.html")
ANNOUNCEMENT_FILES=("index.html")

source venv/bin/activate
python3 assets/scripts/navbar.py ${NAVBAR_FILES[*]}
echo "Finished assembling navbar in ${NAVBAR_FILES[*]}"
python3 assets/scripts/announcements.py ${ANNOUNCEMENT_FILES[*]} ${WEEKS[*]}
echo "Finished assembling announcements in ${ANNOUNCEMENT_FILES[*]}"
deactivate

grep -rl "{% SEMESTER %}" temp/ | xargs sed -i "" -e "s/{% SEMESTER %}/${SEMESTER}/g"
echo "Finished inserting semester"
cp temp/* .
echo "Finished publishing all files"
