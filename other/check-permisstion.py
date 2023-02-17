#!/usr/bin/python2
import os
import sys
import grp
import pwd

filename =  sys.argv[1]
import glob
# Recursively fetch all txt files from given path
# for filepath in glob.iglob(filename , recursive=True):
#  print(filepath)
# check permission and file group, owner, makit to a list
# then run all to set right permission

# that safer than set permission very long run (cannot track)

# print(filename)

# 
def find_path(dir_):
    for root, folders, names in os.walk(dir_):
        print(folders)
        for name in names:
            print(name)
            if name.endswith(".html"):
                # Your code
                pass

def find_loop(dir):
    for dirpath, dirs, files in os.walk(dir): 
        for filename in files:
            fname = os.path.join(dirpath,filename)
            # if (fname.endswith('.php')
            #     or fname.endswith(".html")
            #     or fname.endswith(".htm")):
            #     print(fname)
            print(fname)
            

# find_path(filename)
# find_loop(filename)
def get_owner(stat_info):
    uid = stat_info.st_uid
    owner = pwd.getpwuid(uid)[0]
    return owner

def get_group(stat_info):
    gid = stat_info.st_gid
    group = grp.getgrgid(gid)[0]
    return group

stat_info = os.stat(filename)

uid = pwd.getpwnam("www").pw_uid
gid = grp.getgrnam("www").gr_gid

print uid, gid
os.chown(filename + "/text_test.html", uid, gid)
# os.chown("filename + "/text_test.html"", uid, gid)


# stat_info = os.stat(filename)
# uid = stat_info.st_uid
# gid = stat_info.st_gid
# print uid, gid

# user = pwd.getpwuid(uid)[0]
# group = grp.getgrgid(gid)[0]
# print user, group
