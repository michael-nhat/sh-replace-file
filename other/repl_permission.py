
#!/usr/bin/python2
import os
import sys
import grp
import pwd

homedir = "/root"
filename = "/root/.find"
filename_stat = os.stat(filename)
print(homedir)
f = open(homedir + "/list-need-fix.txt", "w")
import glob

uid = pwd.getpwnam("www").pw_uid
gid = grp.getgrnam("www").gr_gid

print(uid, gid)



# file1 = filename + "/text_test.html"
# file1stat = os.stat(file1)
# filename_stat = os.stat(filename)

# find_path(filename)
# find_loop(filename)

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

# set_permission(filename)

# set_permission(file1)

# mask = oct(os.stat(file1).st_mode)[-3:]

# Print the mask
# print(file1)

print("File permission mask:"
      ,check_permission(filename_stat)
      , get_permission_mask_code(filename_stat))

# stat_info = os.stat(filename)
# os.chown(file1, uid, gid)

# # print(stat_info)
# # print(file1)

# os.chown(filename + "/text_test.html", uid, gid)
# import subprocess
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

def find_loop(dir):
    for dirpath, dirs, files in os.walk(dir): 
        d_stat = os.stat(dirpath)
        if not (check_permission(d_stat)
                and check_owner_group(d_stat)):
            print(dirpath + "/")
            f.write(dirpath + "/" +"\n")
        for filename in files:
            fname = os.path.join(dirpath, filename)
            f_stat = os.stat(fname)
            if find_type_check(fname):
                if not (check_owner_group(f_stat)
                    and check_permission(f_stat)):
                    print(fname)
                    f.write(fname + "\n")

            # unless check correct owner, group permisstion, set
            # unless check correct permission, set
            # print(fname)
