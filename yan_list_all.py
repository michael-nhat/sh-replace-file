#!/usr/bin/python2
import os
import sys;
# step 1:
# list all file contain one (in the list)
# write to file  >> then check many file to test (could print file and the containt tag to see , or st)

# step 2:
# run delete script

# mobile is same as pc, script must work for both?
# or mobile and PC should separate to make it simple?
# mobile could contain PC, PC could contain mobile link, this don't affect
# mobile or pc, each has just one kind of tag contain

match_regex_pattern = ['/TheWorldCup', '/zuqiubifen', '/zuqiuzhibo', '/maiqiu', '/jingcai', '/jc']

# fileInName = sys.argv[1]

current_dir =  sys.argv[1]
print("aa", current_dir)

# print all

# for pc: loop in all file except folder current_folder/m
