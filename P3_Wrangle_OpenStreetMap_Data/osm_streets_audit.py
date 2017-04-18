#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
We used iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.

Next task task for this code  has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    We have added mappings only for the actual problems encountered in OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
    
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

"""
This script checks for incosistent and erroneous street types in the amsterdam openstreet map
Then we created a list with the street types that we expect to see in our dataset

"""
osmfile = "amsterdam_netherlands.osm"
street_re = re.compile(r'\S+(\s\S+)*')
streets = defaultdict(set)


expected_streets = ["achterburgwal", "baan", "dam", "dijk", "gracht",
                      "haven",  "hof", "hoje",  "kade", "laan", "markt", "pad", "plein", "schans",
                      "straat", "voorburgwal", "weg", "dreef"]

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


def audit_streets(streets, street_name):
    """ 
    We create a function that will audit for non expected street types
    
    """ 
    n = street_re.search(street_name)
    if n:
        street_found = n.group()
        if street_found not in expected_streets:
        	streets[street_found].add(street_name)


def is_street(elem):
    return (elem.attrib['k'] == "addr:street")

def audit_street(osmfile):
    street_types = defaultdict(set)
    for elem in get_element(osmfile):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street(tag):
                    audit_streets(streets, tag.attrib['v'])
                    update_street_type(tag.attrib['v'],mapping)
    pprint.pprint(dict(streets))


#audit_street(osmfile)
"""
We create a dictionary that keeps track of the changes needed to be done to fix 
the unexpected street types.

"""
mapping = { 
                "de ": "De",
                "tt.": "Tt.",
                "passage" : "Passage",
                "mees": "Mees",
                "Overweerse polderdijk": "Overweersepolderdijk",
                "mt.": "Mt.",
                "boulevard": "Boulevard",
                "mees": "Mees",
                "wielewaallaan": "Wielewaallaan"
    }

"""

Now its time to create the function that will fix the erroneous street types.
We will use it in the data.py script to create the final dictionaries that would
be used to write the appropriate .csv files. Before doing this we will also use
the title method to modify any capitalize street type.

"""
def update_street_type(name, mapping):
    m = street_re.search(name)
    if m:
        street_type = m.group()
        if  street_type in mapping.keys():
            print 'Before: ' , name
            name = re.sub(m.group(), mapping[m.group()], name)
            print 'After: ', name
    return name

if __name__ == '__main__':
    audit_street(osmfile)
