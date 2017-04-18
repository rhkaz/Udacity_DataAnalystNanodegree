#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
We used iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
We wanted to correct postal code format separate the integers from character duplo with a space.

Next task task for this code has follwing steps:

- audit the OSMFILE and change the variable postcode to reflect the changes needed to fix 
    the unexpected postcodes types to the appropriate ones.
    We have added postcodes for the actual problems encountered in OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- used regular expressions as a tool to approach this problem.
    For example, postal codes in the Ntherlands have a basic fourvdigit format 
    follwoed by space and then two letters. I used the standard format
    to be matched against each record in OSM dataset:        
- write the clean_postcode function, to actually fix the street name.   

"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

streets = defaultdict(set)

post_file='amsterdam_netherlands.osm'   

POSTCODE = re.compile(r'^[1-9][0-9]{3}\s?[a-zA-Z]{2}$$')


def is_zip_code(elem):
	return (elem.attrib['k'] == "addr:postcode")

#Incomplete and incorrect postal codes

"""
Discard postal codes that are not in the correct Netherlands format, i.e.,
1000 AA, where 4 integers are followed by a space and then 2 letters.
 
"""

def clean_postcode(postcode):
    m = POSTCODE.search(postcode)
    if m:
        if " " not in postcode:
            postcode = postcode[:4] + " " + postcode[4:]
        return postcode
    else:
        if postcode != POSTCODE:
            return None    


def audit_postcode(post_file):
    postcode_set = set()
    for event, elem in ET.iterparse(post_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'addr:postcode':
                    post_code = tag.attrib['v'].strip()
                    
                    m = POSTCODE.search(post_code)
                    if m:
                        #print post_code
                        pass
                        #print clean_postcode(post_code)    
                    else:
                        postcode_set.add(post_code)
    return postcode_set

postcode_set = audit_postcode(post_file)
