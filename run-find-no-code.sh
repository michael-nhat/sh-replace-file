#!/bin/bash
find-no-code () {
    if grep -q 'a87ff42a01e584a69e3421eecad7cb31' "$1"; then
    # check if 2 script, delete one, then replace one
        if [[ $(grep $1 -e "hm.src =" | wc -l) -gt 1 ]];
        then 
            echo "found 2 script: $1 need delete one and replace one";
            ./delete-1-script.py $1; 
            ./awk-replace.awk $1  | sponge $1;
        else
        true;
        # echo "has right script: $1";
        fi
    else if grep -q 'hm.src =' "$1"; then
        echo "has script but no right code: $1";
        # replace here
        ./awk-replace.awk $1  | sponge $1;
        else
        echo "need insert script: $1";
        ./insert-script.py $1;
        fi
    fi
}

count=0; find $1 -name "*.html" | while read i; do count=$((count+1));  echo $count; find-no-code $i; done

