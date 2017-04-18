#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:51:02 2017

@author: RashidKazmi
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

streets = defaultdict(set)

post_file='amsterdam_netherlands_full.osm'   

POSTCODE = re.compile(r'^[1-9][0-9]{3}\s?[a-zA-Z]{2}$$')

#zip_codes = []

def is_zip_code(elem):
	return (elem.attrib['k'] == "addr:postcode")


def clean_postcode(postcode):
    m = POSTCODE.search(postcode)
    #     if m is not None:
    # use:
    if m:
        if " " not in postcode:
            postcode = postcode[:4] + " " + postcode[4:]
            #zip_codes.append(postcode)
        return postcode
    else:
    
        if postcode != POSTCODE:
            return None    


def audit_postcode(post_file):
    # save the postcodes that you need to clean:
    postcode_set = set()
    for event, elem in ET.iterparse(post_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'addr:postcode':
                    # why are you removing the spaces?
                    post_code = tag.attrib['v']
                    
                    m = POSTCODE.search(post_code)
                    if m:
                        print post_code
                        pass
                        #print clean_postcode(post_code)    
                    else:
                        postcode_set.add(post_code)
    return postcode_set

postcode_set = audit_postcode(post_file)
