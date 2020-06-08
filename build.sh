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

SEMESTER="Summer 2020"
WEEKS=(1)
SURVEY="https://forms.gle/thhtwLmhEGgTbYkC7"
VERSION="v1.0.1"

NAVBAR_FILES=("index.html" "about.html")
INDEX_FILES=("index.html")
CALENDAR_FILES=("index.html")
FOOTER_FILES=("index.html" "about.html")

mkdir -p temp
source venv/bin/activate
python3 assets/scripts/navbar.py ${NAVBAR_FILES[*]}
echo "Finished assembling navbar in ${NAVBAR_FILES[*]}"
python3 assets/scripts/announcements.py ${CALENDAR_FILES[*]} ${WEEKS[*]}
echo "Finished assembling announcements in ${CALENDAR_FILES[*]}"
python3 assets/scripts/accordian.py ${WEEKS[*]}
echo "Finished assembling weekly schedule in ${INDEX_FILES[*]}"
python3 assets/scripts/footer.py ${FOOTER_FILES[*]}
echo "Finished assembling footer in ${FOOTER_FILES[*]}"
deactivate

grep -rl "{% SURVEY %}" temp/ | xargs sed -i -e "s,{% SURVEY %},${SURVEY},g"
echo "Finished inserting anonymous survey links"
grep -rl "{% SEMESTER %}" temp/ | xargs sed -i -e "s/{% SEMESTER %}/${SEMESTER}/g"
echo "Finished inserting semester"
grep -rl "{% VERSION %}" temp/ | xargs sed -i -e "s,{% VERSION %},${VERSION},g"
echo "Finished updating version"
cp temp/* .
echo "Finished publishing all files"
