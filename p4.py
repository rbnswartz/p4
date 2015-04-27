#!/bin/python
import xml.etree.ElementTree as et
import sys
import os

def usage():
    print "Usage: "
    print "p4444.py <file path of PublishProfile file>"

def parse(path):
    path = os.path.abspath(sys.argv[1])
    print "Opening " + path + "\n"
    doc = et.parse(path)
    root = doc.getroot()
    element = root.findall("publishProfile[@publishMethod='FTP']")[0]
    print "Server " + element.attrib["publishUrl"]
    print "User " + element.attrib["userName"]
    print "Password " + element.attrib["userPWD"]

def main():
    if len(sys.argv)> 1:
        parse(sys.argv[1])
    else:
        usage()

main()
