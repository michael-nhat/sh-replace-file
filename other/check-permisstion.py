#!/usr/bin/python2
import os
import sys
import grp
import pwd
import glob
import subprocess
import file_util as fu

filename =  sys.argv[1]
homedir = sys.argv[2]
# print(homedir)

filename_stat = os.stat(filename)
# overwrite
f = open(homedir + "/list-need-fix.txt", "w")
# f.write("abc")
# put side affect only at control 

# Recursively fetch all txt files from given path
# for filepath in glob.iglob(filename , recursive=True):
#  print(filepath)
# check permission and file group, owner, makit to a list
# then run all to set right permission

# that safer than set permission very long run (cannot track)

# print(filename)

# set_permission(filename)

# set_permission(file1)

# mask = oct(os.stat(file1).st_mode)[-3:]

# Print the mask
# print(file1)

print("File permission mask:"
      , fu.check_permission(filename_stat)
      , fu.get_permission_mask_code(filename_stat))

# stat_info = os.stat(filename)

# uid = pwd.getpwnam("www").pw_uid
# gid = grp.getgrnam("www").gr_gid

# print(uid, gid)

# os.chown(file1, uid, gid)

# # print(stat_info)
# # print(file1)

# os.chown(filename + "/text_test.html", uid, gid)
# p = subprocess.Popen("chgrp root " + file1, stdout=subprocess.PIPE, shell=True,
#                      executable="/bin/bash")

# print(p.communicate())


# p = subprocess.Popen("ls -la " + file1, stdout=subprocess.PIPE, shell=True,
#                      executable="/bin/bash")

# print(p.communicate())

# info1 = os.stat(file1)
# print(get_group(info1), get_owner(info1))

# stat_info = os.stat(filename)
# uid = stat_info.st_uid
# gid = stat_info.st_gid
# print uid, gid

# user = pwd.getpwuid(uid)[0]
# group = grp.getgrgid(gid)[0]
# print user, group

# with ntfs share, chmod, chgr don't work

            # unless check correct owner, group permisstion, set
            # unless check correct permission, set
            # print(fname)

def find_loop(dir):
    for dirpath, dirs, files in os.walk(dir): 
        d_stat = os.stat(dirpath)
        if not (fu.check_permission(d_stat)
                and fu.check_owner_group(d_stat)):
            print(dirpath + "/")
            f.write(dirpath + "/" +"\n")
        for filename in files:
            fname = os.path.join(dirpath, filename)
            f_stat = os.stat(fname)
            if fu.find_type_check(fname):
                if not (fu.check_owner_group(f_stat)
                    and fu.check_permission(f_stat)):
                    print(fname)
                    f.write(fname + "\n")

find_loop(filename)
print(1)

# run sudo, so he is root, home is /root
# print(os.getenv("HOME"))

f.close()
