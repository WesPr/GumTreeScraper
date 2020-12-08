from bs4 import BeautifulSoup
import requests

#Last page number
end_page_num = 25
i = 2

names = []
prices = []
urls = []

#Opening of csv file
filename = "ps4.csv"
f = open(filename, "w")

headers = "Title, Price\n"

f.write(headers)

websiteUrl = "https://www.gumtree.co.za/s-playstation-consoles/v1c9510p1?q=ps4"
r = requests.get(websiteUrl)
data = r.text
soup = BeautifulSoup(data)
listings = soup.findAll("div", {"class": "related-ad-content"})
print("Finding your PS4...")
for listing in listings:
    name = listing.div.a.span.text
    price_container = listing.find("div", {"class": "price"})
    url_container = listing.find("a", {"class": "related-ad-title"})
    url = url_container.get('href')
    price = price_container.text
    price = price.replace("  ", "")
    price = price.replace("\n", "")
    price = price.replace("R", "")
    price = price.replace(",", "")
    if (price != "Contact for Price"):
        if (price != "Swap/Trade"):
            if (price != "Negotiable"):
                price = int(price)
                if (price <= 3000):
                    names.append(name)
                    prices.append(price)
                    urls.append(url)

while i <= end_page_num:
    websiteUrl = "https://www.gumtree.co.za/s-playstation-consoles/page-" + str(i) + "/v1c9510p" + str(i) + "?q=ps4"
    r = requests.get(websiteUrl)
    data = r.text
    soup = BeautifulSoup(data)
    listings = soup.findAll("div", {"class": "related-ad-content"})

    for listing in listings:
        name = listing.div.a.span.text
        price_container = listing.find("div", {"class": "price"})
        url_container = listing.find("a", {"class": "related-ad-title"})
        url = url_container.get('href')
        price = price_container.text
        price = price.replace("  ", "")
        price = price.replace("\n", "")
        price = price.replace("R", "")
        price = price.replace(",", "")
        if (price != "Contact for Price"):
            if (price != "Swap/Trade"):
                if (price != "Negotiable"):
                    price = int(price)
                    if (price <= 3000):
                        names.append(name)
                        prices.append(price)
                        urls.append(url)
    i += 1

list_size = len(prices)
x = 0
while x < list_size:
    f.write(names[x].replace(",", "|") + "," + str(prices[x]).replace(",", "") + "," + "https://www.gumtree.co.za/"+urls[x].replace(",", "") + "\n")
    x +=1

f.close()
