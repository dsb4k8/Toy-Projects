import requests
from bs4 import BeautifulSoup as bsp
from pprint import pprint

class Show():
    def __init__(self, title):
        self.name = title
        # Plug in network information 
        self.network = ""
    def __repr__(self):
        return unicode("\n\nTitle: {}\nNetwork: {}\n\n").format(self.name, self.network).encode('utf-8')

def get_sling_networks():
    data = "https://www.cnet.com/news/sling-tv-everything-you-need-to-know/"
    response  = requests.get(data, timeout=5)
    content = bsp(response.content, "html.parser")
    data_container = content.find("div", class_ = "chartWrapper")

    target = data_container.findAll("th")
    for i in target:
        print i.getText().strip()
 


if __name__=="__main__":

    get_sling_networks()

