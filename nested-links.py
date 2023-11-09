from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctxt = ssl.create_default_context()
ctxt.check_hostname = False
ctxt.verify_mode = ssl.CERT_NONE

inp = input("Enter URL: ")
link_pos = int(input("Enter position: "))
repetitions = int(input("Enter repetitions: "))

anchor_dict = dict()
name_dict = dict()


def get_links():
    def the_link(link):
        html = urlopen(link, context=ctxt).read()
        return BeautifulSoup(html, "html.parser")("a")

    counter = repetitions
    Link = inp

    while counter > 0:
        anchors = the_link(Link)
        for indx, anchor in enumerate(anchors):
            anchor_links = "".join(re.findall(r'(http.+?)">', str(anchor)))
            anchor_names = "".join(re.findall(r">(.+?)<", str(anchor)))
            anchor_dict[indx] = anchor_links
            name_dict[anchor_links] = anchor_names

        Link = anchor_dict.get(link_pos - 1, None)
        name = name_dict.get(Link)
        counter -= 1
    return name


res = get_links()
print(res)
