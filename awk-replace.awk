#!/bin/awk -f
BEGIN {
}

{
    targetReplace = "hm.src = \"https://hm.baidu.com/hm.js?a87ff42a01e584a69e3421eecad7cb31\";";
    gsub(/hm.src = "[^"]*";/, targetReplace);
    print;
}

END{
}


# regex nhan dien duoc
# thay the thi thay the cai dau tien, hay la tat ca
# hay la no cung khong quan trong, ok



