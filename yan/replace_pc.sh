#!/bin/bash

# find ./yan_test/ -type f \(  -name "*.html" -o -name "*.htm" \) | xargs grep -l -e '<li class="item"><a href="http://www.tvyan.com/TheWorldCup/">世界杯</a></li>' -e '<li class="item"><a href="http://www.tvyan.com/TheWorldCup/sjbqd/">国家队</a></li>' -e '<li class="item"><a href="http://www.tvyan.com/zuqiubifen/">足球比分</a></li>' -e '<li class="item"><a href="http://www.tvyan.com/zuqiuzhibo/">足球直播</a></li>' > ~/find_need_remove2.txt
## find ./yan_test/ -type f \(  -name "*.html" -o -name "*.htm" \) | xargs grep -rnwl './yan_test/' -e '<a href="http://m.tvyan.com/TheWorldCup/">世界杯</a>' -e '<a href="http://m.tvyan.com/TheWorldCup/sjbqd/">国家队</a>' -e '<a href="http://m.tvyan.com/zuqiubifen/">足球比分</a>' -e '<a href="http://m.tvyan.com/zuqiuzhibo/">足球直播</a>'
 

cat ~/find_need_remove2.txt | while read line;
do echo $line;
   if [[ "$line" == *"bak"* ]]; then
       echo "bak";
   else
       sed -i 's/<li class="item"><a href="http:\/\/www.tvyan.com\/TheWorldCup\/">世界杯<\/a><\/li>//g' $line;
       sed -i 's/<li class="item"><a href="http:\/\/www.tvyan.com\/TheWorldCup\/sjbqd\/">国家队<\/a><\/li>//g' $line;
       sed -i 's/<li class="item"><a href="http:\/\/www.tvyan.com\/zuqiubifen\/">足球比分<\/a><\/li>//g' $line;
       sed -i 's/<li class="item"><a href="http:\/\/www.tvyan.com\/zuqiuzhibo\/">足球直播<\/a><\/li>//g' $line;

   fi;
done
