import codecs
import sys

import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Tag


weeks = [int(w) for w in sys.argv[1:]]
total_weeks = 8

file = codecs.open("./temp/index.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'html.parser')
accordianfile = codecs.open("./templates/accordian.html", "r", "utf-8")
accordian_soup = BeautifulSoup(accordianfile.read(), 'html.parser')

for i in weeks:
    button = accordian_soup.find(id="week%s" % i)

    tree = ET.parse('calendar/week%s.xml' % i)
    root = tree.getroot()
    button.append(root[0].text)

    if i == len(weeks):
        button['class'].remove('collapsed')
        body = accordian_soup.find(id="collapse%i" % i)
        body['class'].append('show')

for i in range(weeks[-1] + 1, total_weeks+1):
    button = accordian_soup.find(id="week%s" % i)
    button['class'].append('disabled')

    tree = ET.parse('calendar/week%s.xml' % i)
    root = tree.getroot()
    button.append(root[0].text)


accordian = soup.find(id="weekly-info")
accordian.append(str(accordian_soup))

stringy = str(soup.prettify())
stringy = stringy.replace('&lt;', '<')
stringy = stringy.replace('&gt;', '>')
outfile = codecs.open("./temp/index.html", "w+", "utf-8")
outfile.write(stringy)
