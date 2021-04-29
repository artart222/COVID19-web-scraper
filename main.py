import requests
from bs4 import BeautifulSoup

URL = "https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

data = {}
number_of_data = 0

for tag in soup.findAll("tr"):
    #  stag = second tag
    list_of_data = []
    for stag in tag.findAll("td"):

        if number_of_data % 4 == 0:
            country = stag.getText()
        elif number_of_data % 4 == 1:
            list_of_data.append(stag.getText())
        elif number_of_data % 4 == 2:
            list_of_data.append(stag.getText())
        else:
            list_of_data.append(stag.getText())
            data[country] = list_of_data

        number_of_data += 1

for keys, values in data.items():
    print(keys, "==> ", "Total cases:", values[0], "Total deaths:", values[1])


save = input("\n\nDo you want save this statistics to a file (yes/no): ")
if save == "yes":
    with open("covid19-statistics.txt", "w") as f:
        for keys, values in data.items():
            string_data = keys + " ==> " + "Total cases: " + values[0] + " Total deaths: " + values[1] + "\n"
            f.write(string_data)
