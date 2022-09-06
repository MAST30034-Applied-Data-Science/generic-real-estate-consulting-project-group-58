import pandas as pd
import os
import requests
import re
import csv
from zipfile import ZipFile
import json

# built-in imports
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 51) # update this to your liking

########################################  domain website scraping  ########################################
# begin code
url_links = []
property_metadata = defaultdict(dict)
# generate list of urls to visit
for page in N_PAGES:
    url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    bs_object = BeautifulSoup(requests.get(
        url, headers=headers).text, "html.parser")
    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
    index_links = bs_object \
        .find(
            "ul",
            {"data-testid": "results"}
        ) \
        .findAll(
            "a",
            href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
        )
    for link in index_links:
        # if its a property address, add it to the list
        if 'address' in link['class']:
            url_links.append(link['href'])
# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    bs_object = BeautifulSoup(requests.get(
    property_url, headers=headers).text, "html.parser")
    # looks for the header class to get property name
    property_metadata[property_url]['name'] = bs_object \
        .find("h1", {"class": "css-164r41r"}) \
        .text
    # looks for the div containing a summary title for cost
    property_metadata[property_url]['cost_text'] = bs_object \
        .find("div", {"data-testid": "listing-details__summary-title"}) \
        .text
    # extract coordinates from the hyperlink provided
    # i'll let you figure out what this does :P
    property_metadata[property_url]['coordinates'] = [
        float(coord) for coord in re.findall(
            r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
            bs_object \
                .find(
                    "a",
                    {"target": "_blank", 'rel': "noopener noreferer"}
                ) \
                .attrs['href']
        )[0].split(',')
    ]
    rooms_list = []
    for feature in bs_object \
            .find("div", {"data-testid": "property-features"}) \
            .findAll("span", {"data-testid": "property-features-text-container"}):
        try:
            rooms_list.append(re.findall(r'\d\s[A-Za-z]+', feature.text)[0])
        except IndexError:
            pass
    property_metadata[property_url]['rooms'] = rooms_list
    # property_metadata[property_url]['rooms'] = [
    #     re.findall(r'\d\s[A-Za-z]+', feature.text)[0] for feature in bs_object \
    #         .find("div", {"data-testid": "property-features"}) \
    #         .findAll("span", {"data-testid": "property-features-text-container"})
    # ]
    property_metadata[property_url]['desc'] = re \
        .sub(r'<br\/>', '\n', str(bs_object.find("p"))) \
        .strip('</p>')
# output to example json in data/raw/
with open('data/raw/example.json', 'w') as f:
    dump(property_metadata, f)
    
########################################   population  ########################################
dls = "https://www.abs.gov.au/statistics/people/population/regional-population/2021/32180DS0001_2001-21.xlsx"
resp = requests.get(dls)
output = open('data/raw/population.xlsx', 'wb')
output.write(resp.content)
output.close()

########################################   SA2  ########################################
dls = "https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files/SA2_2021_AUST_SHP_GDA2020.zip"
resp = requests.get(dls)
# upload SA2.zip
output = open('data/raw/SA2.zip', 'wb')
output.write(resp.content)
output.close()
directory = "data/raw/SA2"
# Parent Directory path 
parent_dir = "data/raw"
path = os.path.join(parent_dir, directory) 
#create folder
os.mkdir(path) 
# save zip to a folder
with zipfile.ZipFile("data/raw/SA2.zip", mode="r") as archive:
    archive.extractall("data/raw/SA2")
    archive.close()
# remove SA2.zip
os.remove("data/raw/SA2.zip")

########################################   ptv  ########################################
dls = "http://data.ptv.vic.gov.au/downloads/gtfs.zip"
resp = requests.get(dls)
# upload gtfs.zip
output = open('data/raw/gtfs.zip', 'wb')
output.write(resp.content)
output.close()
directory = "data/raw/ptv"
# Parent Directory path 
parent_dir = "data/raw"
path = os.path.join(parent_dir, directory) 
#create folder
os.mkdir(path) 
# save zip to a folder
with zipfile.ZipFile("data/raw/gtfs.zip", mode="r") as archive:
    archive.extractall("data/raw/ptv")
    archive.close()
# remove gtfs.zip
os.remove("data/raw/gtfs.zip")

########################################   school locations  ########################################
dls = "https://www.education.vic.gov.au/Documents/about/research/datavic/dv309_schoollocations2021.csv"
resp = requests.get(dls)
output = open('data/raw/school2021.csv', 'wb')
output.write(resp.content)
output.close()

########################################   hospital locations  ########################################
dls = "https://data.humdata.org/dataset/a5221b34-8ed4-4e19-88c9-b195c13502b6/resource/6df0921e-d676-4c36-8229-c65cea510217/download/australia.csv"
resp = requests.get(dls)
output = open('data/raw/hospital2021.csv', 'wb')
output.write(resp.content)
output.close()