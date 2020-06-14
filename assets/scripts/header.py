import codecs
import sys
from bs4 import BeautifulSoup, Tag

files = sys.argv[1:]

for filename in files:
    try:
        file = open("temp/%s" % filename)
    except FileNotFoundError:
        file = open("temp/%s" % filename, 'w')
    finally:
        file.close()

    headfile = codecs.open("./templates/head.html", "r", "utf-8")
    soup_head = BeautifulSoup(headfile.read(), 'html.parser')

    file = codecs.open("./templates/%s" % filename, "r", "utf-8")
    soup = BeautifulSoup(file.read(), 'html.parser')

    head = soup.find(id="head")
    head.append(str(soup_head))

    stringy = str(soup.prettify())
    stringy = stringy.replace('&lt;', '<')
    stringy = stringy.replace('&gt;', '>')
    outfile = codecs.open("./temp/%s" % filename, "w+", "utf-8")
    outfile.write(stringy)