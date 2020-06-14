import codecs
import sys
from bs4 import BeautifulSoup, Tag

files = sys.argv[1:]

file_to_id = {
    "index.html" : "nav-bar-index",
    "about.html" : "nav-bar-about",
}

for filename in files:
    navbarfile = codecs.open("./templates/navbar.html", "r", "utf-8")
    soup_bar = BeautifulSoup(navbarfile.read(), 'html.parser')
    active_el = soup_bar.find(id=file_to_id[filename])
    active_el['class'].append('active')

    file = codecs.open("./temp/%s" % filename, "r", "utf-8")
    soup = BeautifulSoup(file.read(), 'html.parser')

    navbar = soup.find(id="navbar")
    navbar.append(str(soup_bar))

    stringy = str(soup.prettify())
    stringy = stringy.replace('&lt;', '<')
    stringy = stringy.replace('&gt;', '>')
    outfile = codecs.open("./temp/%s" % filename, "w+", "utf-8")
    outfile.write(stringy)
