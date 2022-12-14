import pandas as pd
import requests
import os
import re
import csv
from zipfile import ZipFile
import zipfile
import json
from collections import defaultdict
from bs4 import BeautifulSoup
from json import dump
from urllib.request import urlopen



# built-in imports
headers = {"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
# constants
BASE_URL = "https://www.domain.com.au"
#N_PAGES = range(1, 51) # update this to your liking
Postcode = range(3000, 4000)


########################################  domain website scraping  ########################################
# begin code
url_links = []
property_metadata = defaultdict(dict)
# generate list of urls to visit
for postcode in Postcode:
    #url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"

    url = BASE_URL + f"/rent/?excludedeposittaken=1&postcode={postcode}"
    bs_object = BeautifulSoup(requests.get(
        url, headers=headers).text, "html.parser")
    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
    try:
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
    except AttributeError:
        pass
    
    
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
with open('../data/raw/domain1.json', 'w') as f:
    dump(property_metadata, f)