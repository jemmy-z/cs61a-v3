import codecs
import sys
from bs4 import BeautifulSoup, Tag

files = sys.argv[1:]
navbarfile = codecs.open("./templates/navbar.html", "r", "utf-8")
soup_bar = BeautifulSoup(navbarfile.read(), 'html.parser')

for filename in files:
    try:
        file = open("temp/%s" % filename)
    except IOError:
        file = open("temp/%s" % filename, 'w+')
    finally:
        file.close()
    file = codecs.open("./templates/%s" % filename, "r", "utf-8")
    soup = BeautifulSoup(file.read(), 'html.parser')

    navbar = soup.find(id="navbar")
    navbar.append(str(soup_bar))

    stringy = str(soup.prettify())
    stringy = stringy.replace('&lt;', '<')
    stringy = stringy.replace('&gt;', '>')
    outfile = codecs.open("./temp/%s" % filename, "w+", "utf-8")
    outfile.write(stringy)
