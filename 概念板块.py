import requests
from bs4 import BeautifulSoup
import bs4
url='https://q.stock.sohu.com/cn/bk.shtml?spm=stockpc.home.navi.2.1603949083181kAAg2im'
html = requests.get(url)
html.encoding=html.apparent_encoding
main_page = BeautifulSoup(html.text, "html.parser")
table = main_page.find_all(name="a")[32:]
fa="D:/concept.csv"

for p in table:
    print(p.text)
    with open(fa, 'a') as f:
        f.write(p.text)
        f.write('\n')