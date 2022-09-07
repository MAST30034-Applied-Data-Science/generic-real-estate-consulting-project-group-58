import pandas as pd
import requests
import os
import re
import csv
# from zipfile import ZipFile
import zipfile
import json

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
#directory = "data/raw/SA2"
# Parent Directory path 
# parent_dir = "data/raw"
# = os.path.join(parent_dir, directory) 
path = "data/raw/SA2"
#create folder
#os.mkdir(path) 
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
# directory = "data/raw/ptv"
# Parent Directory path 
path = "data/raw/ptv"
# path = os.path.join(parent_dir, directory) 
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