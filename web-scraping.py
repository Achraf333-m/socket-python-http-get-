# I got a website with a table filled with data, I want to access the website and pull the numbers in each data row so I can sum them up.

# (((   import sys
# sys.path.insert(1, r'C:\Users\achra\.vscode\extensions\ms-python.vscode-pylance-2023.11.10\dist\typeshed-fallback\stubs\beautifulsoup4\bs4\__init__.pyi')
# ^^^^ in case the file directory is not in path. ))))

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# here I am ignoring the ssl certifications so I can pull data from https.

contxt = ssl.create_default_context()
contxt.check_hostname = False
contxt.verify_mode = ssl.CERT_NONE

url = input('Enter the url: ')
html = urlopen(url, context=contxt).read()
soup = BeautifulSoup(html, "html.parser")


# now I am retrieving all of the span elements on that website.
def sum_int_table():
    sum = 0
    spans = soup("span")
    for span in spans:
        # using regex to find the character that match the criteria: any one or more digits
        num_list = re.findall("[0-9]+", str(span))
        # turning the list into a string then into an integer
        int_num = int("".join(num_list))
        sum += int_num
    return sum

numSum = sum_int_table()

print(numSum)