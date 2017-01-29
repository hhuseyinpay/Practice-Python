#!/usr/bin/env python2
# coding: utf-8
from bs4 import BeautifulSoup
import urllib2

word = raw_input("Kelimeyi girin: ").lower()

page_source = urllib2.urlopen("http://tureng.com/tr/turkce-ingilizce/"+word).read()
soup = BeautifulSoup(page_source,"lxml").find("table",{"class":"table table-hover table-striped searchResultsTable"}).findAll("a")

definitionpagesource = urllib2.urlopen("https://en.oxforddictionaries.com/definition/"+word).read()
definition = BeautifulSoup(definitionpagesource,"lxml").find("span",{"class":"ind"}).string

print ("-------  " + word + ": "+definition+"  -------")

final = soup
counter = 7
for x in final:
    if x.string != word:
        if counter != 0:
            print (x.string)
            counter = counter - 1
