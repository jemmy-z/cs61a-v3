import codecs
import sys
from bs4 import BeautifulSoup, Tag

files = sys.argv[1:]

footerfile = codecs.open("./templates/footer.html", "r", "utf-8")
soup_footer = BeautifulSoup(footerfile.read(), 'html.parser')

for filename in files:
    file = codecs.open("./temp/%s" % filename, "r", "utf-8")
    soup = BeautifulSoup(file.read(), 'html.parser')

    footer = soup.find(id="footer")
    footer.append(str(soup_footer.prettify()))

    stringy = str(soup.prettify())
    stringy = stringy.replace('&lt;', '<')
    stringy = stringy.replace('&gt;', '>')
    outfile = codecs.open("./temp/%s" % filename, "w+", "utf-8")
    outfile.write(stringy)
