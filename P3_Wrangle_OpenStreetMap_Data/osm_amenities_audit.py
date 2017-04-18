#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 15:27:30 2017

@author: RashidKazmi
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

# We are following the same procedure as in the osm_audit_street_type.py
# script, but this time we will audit and update amenities. The only difference
# with the audit_street_type.py script is that we won't use the title method
# because the amenities names are found in lowercase letters in the OpenStreetMap
# dataset.

osmfile = "amsterdam_netherlands.osm"
amenity_re = re.compile(r'\S+(\s\S+)*')
amenities = defaultdict(set)


expected_amenities = ["ambulance_station", "arts_center", "atm", "bank", "bar",
                        "beauty salon", "bowling club", "bus_station", "cafe",
                        "car_rental", "casino", "cinema","club", "club_house", 
                        "college","dentist", "doctors", "fast_food",
                        "fire_station", "fuel", "hospital", "nightclub", "park", 
                        "pharmacy", "police", "post_office", "pub", 
                        "restaurant", "school", "taxi", "telephone", "taxi", 
                        "theatre", "university"]

def get_element(osmfile, tags=('node', 'way', 'relation')):
    """ Reference:
    http://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
    """
    context = ET.iterparse(osmfile, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end':
            yield elem
            root.clear()

			
def audit_amenities(amenities, amenity_name):
    n = amenity_re.search(amenity_name)
    if n:
        amenity_found = n.group()
        if amenity_found not in expected_amenities:
        	amenities[amenity_found].add(amenity_name)

def is_amenity(elem):
    return (elem.attrib['k'] == "amenity")

def audit_amenity(osmfile):
    street_types = defaultdict(set)
    for elem in get_element(osmfile):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_amenity(tag):
                    audit_amenities(amenities, tag.attrib['v'])
                    # call update_amenity() function:
                    update_amenity(tag.attrib['v'],amenity_mapping)
    #pprint.pprint(dict(amenities))


#audit_amenity(osmfile)

amenity_mapping = {
                    "Art": "art",
                    "grand Cafe": "grand_cafe", 
                    "Mortgage bank": "mortgage_bank",
                    "doctors;pharnacy;dentist": "medisch_centrum",
                    "first aid": "first_aid",
                    "lock_door storage": "lockers",
                    "Broker": "broker",
                    "Healthcare": "healthcare",
                    "Wellness" : "wellness"
    		      }

def update_amenity(name, mapping):
    m = amenity_re.search(name)
    if m:
        amenity_type = m.group()
        if  amenity_type in mapping.keys():
            print 'Before: ' , name
            name = re.sub(m.group(), mapping[m.group()], name)
            print 'After: ', name
    return name

if __name__ == '__main__':
    audit_amenity(osmfile)
