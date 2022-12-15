#!/bin/bash
find-no-code () {
    if grep -q 'a87ff42a01e584a69e3421eecad7cb31' "$1"; then
    echo "has right script: $1";
    true;
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

count=0; find $(pwd) -name "*.html" | while read i; do count=$((count+1));  echo $count; find-no-code $i; done

