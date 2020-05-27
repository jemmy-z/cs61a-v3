import codecs
from bs4 import BeautifulSoup, Tag


try:
    f = open("temp/index.html")
    f2 = open("temp/about.html")
except IOError:
    f = open("temp/index.html", 'w+')
    f2 = open("temp/about.html", 'w+')
finally:
    f.close()
    f2.close()

mainfile = codecs.open("./templates/index.html", "r", "utf-8")
soup = BeautifulSoup(mainfile.read(), 'html.parser')

navbarfile = codecs.open("./templates/navbar.html", "r", "utf-8")
soup_bar = BeautifulSoup(navbarfile.read(), 'html.parser')

navbar = soup.find(id="navbar")
navbar.append(str(soup_bar))

stringy = str(soup.prettify())
stringy = stringy.replace('&lt;', '<')
stringy = stringy.replace('&gt;', '>')
outfile = codecs.open("./temp/index.html", "w+", "utf-8")
outfile.write(stringy)
