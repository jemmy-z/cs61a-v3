import codecs
import sys

import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Tag


weeks = [int(w) for w in sys.argv[1:]]
total_weeks = 11

file = codecs.open("./temp/index.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'html.parser')
accordianfile = codecs.open("./templates/accordian.html", "r", "utf-8")
accordian_soup = BeautifulSoup(accordianfile.read(), 'html.parser')

for i in weeks:
    tree = ET.parse('calendar/week%s.xml' % i)
    root = tree.getroot()

    button = accordian_soup.find(id="week%s" % i)
    if i == weeks[-1]:
        button['class'].remove('collapsed')
        body = accordian_soup.find(id="collapse%i" % i)
        body['class'].append('show')
    button.append(root[0].text)

    for column in root[1:]:
        materials = accordian_soup.find(id="materials%s" % i)
        col = accordian_soup.new_tag("div")
        col['class'] = ['col-md-6']

        header = accordian_soup.new_tag("h5")
        header.string = column.text
        col.append(header)
        col.append(accordian_soup.new_tag("hr"))

        for section in column:
            title = accordian_soup.new_tag("span")
            title.string = section.text.rstrip()
            col.append(title)
            list = accordian_soup.new_tag("ul")
            listItem = accordian_soup.new_tag("li")

            for item in section:
                lk = accordian_soup.new_tag("a")
                lk['class'] =  ['bordered']
                lk.string = item.text.rstrip()
                lk['href'] = item[0].text.rstrip()
                lk['target'] = ['_blank']
                if item[1].text == "True":
                    lk['class'].extend(['btn-link', 'disabled'])
                listItem.append(lk)
            list.append(listItem)
            col.append(list)
        materials.append(col)

# print(accordian_soup.prettify())

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
