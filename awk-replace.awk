#!/bin/awk -f
BEGIN {
}  
{   
    targetReplace = "hm.src = \"https://hm.baidu.com/hm.js?a87ff42a01e584a69e3421eecad7cb31\";";
    gsub(/hm.src = "https:\/\/hm.baidu.com\/hm.js?[^"]*";/, targetReplace);
    print;
}       
END{
}    