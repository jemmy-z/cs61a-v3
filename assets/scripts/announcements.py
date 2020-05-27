import codecs
import re
import sys
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup, Tag

weeks = [int(w) for w in sys.argv[1:]]

file = codecs.open("./temp/post-nav.html", "r", "utf-8")
soup = BeautifulSoup(file.read(), 'html.parser')

announcements = soup.find(id="carousel-announcements")
wheel = soup.find(id="carousel-indicators")

for i in range(len(weeks)):
    wheel_tag = soup.new_tag("li")
    wheel_tag['data-target']=['#Announcements']
    wheel_tag['data-slide-to']=[str(i)]

    announcement_tag = soup.new_tag("div")
    announcement_tag['id']=["announcement-%s" % (i)]
    announcement_tag['class'] = ['carousel-item', 'p-4']


    if i == len(weeks) - 1:
        print("Currently on Week #%d" % (i+1))
        announcement_tag['class'].append('active')
        wheel_tag['class'] = ['active']

    wheel.append(wheel_tag)
    announcements.append(announcement_tag)

    announcement = soup.find(id="announcement-%s" %(i))

    tree = ET.parse('announcements/week%s.xml' % (weeks[i]))
    root = tree.getroot()
    tag = soup.new_tag("h1")
    tag.string = root[0].text
    announcement.append(tag)

    ul_tag = soup.new_tag("ul")
    ul_tag['class'] = ['announcement-list']
    announcement.append(ul_tag)
    for j in range(1, len(root)):
        li_tag = soup.new_tag("li")
        li_tag['class'] = ['announcement-item']
        li_tag.string = root[j].text
        ul_tag.append(li_tag)

stringy = str(soup.prettify())
stringy = stringy.replace('&lt;', '<')
stringy = stringy.replace('&gt;', '>')
file = codecs.open("index.html", "w", "utf-8")
file.write(stringy)
