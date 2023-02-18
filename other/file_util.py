#!/usr/bin/python2
import os
import sys
import grp
import pwd
import glob
import subprocess

uid = pwd.getpwnam("www").pw_uid
gid = grp.getgrnam("www").gr_gid

def find_path(dir_):
    for root, folders, names in os.walk(dir_):
        print(folders)
        for name in names:
            print(name)
            if name.endswith(".html"):
                # Your code
                pass

def find_type_check(fname):
    return (fname.endswith('.php')
     or fname.endswith(".html")
     or fname.endswith(".htm"))

# file1 = filename + "/text_test.html"
# file1stat = os.stat(file1)

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

def check_owner_group(stat_info):
    return (get_owner(stat_info) == "www" and
            get_group(stat_info) == "www")

def get_permission_mask_code(stat_info):
    return oct(stat_info.st_mode)[-3:]

TARGET_MASK = 0755

def check_permission(stat_info):
    return (get_permission_mask_code(stat_info) == "755")

def set_permission(filepath):
    os.chmod(filepath, 0755)
    return

def set_owner_group(filepath):
    os.chown(filepath, uid, gid)
    return

