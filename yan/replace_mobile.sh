#!/bin/bash

# find ./yan_test/ -type f \(  -name "*.html" -o -name "*.htm" \) | xargs grep -l -e '<a href="http://m.tvyan.com/TheWorldCup/">世界杯</a>' -e '<a href="http://m.tvyan.com/TheWorldCup/sjbqd/">国家队</a>' -e '<a href="http://m.tvyan.com/zuqiubifen/">足球比分</a>' -e '<a href="http://m.tvyan.com/zuqiuzhibo/">足球直播</a>' > ~/file_need_remove.txt
## find ./yan_test/ -type f \(  -name "*.html" -o -name "*.htm" \) | xargs grep -rnwl './yan_test/' -e '<a href="http://m.tvyan.com/TheWorldCup/">世界杯</a>' -e '<a href="http://m.tvyan.com/TheWorldCup/sjbqd/">国家队</a>' -e '<a href="http://m.tvyan.com/zuqiubifen/">足球比分</a>' -e '<a href="http://m.tvyan.com/zuqiuzhibo/">足球直播</a>'
 

cat ~/file_need_remove.txt | while read line;
do echo $line;
   if [[ "$line" == *"bak"* ]]; then
       echo "It's there."
   fi;
   sed -i 's/<a href="http\:\/\/m.tvyan.com\/TheWorldCup\/">世界杯<\/a>//g' $line;
   sed -i 's/<a href="http\:\/\/m.tvyan.com\/TheWorldCup\/sjbqd\/">国家队<\/a>//g' $line;
   sed -i 's/<a href="http\:\/\/m.tvyan.com\/zuqiuzhibo\/">足球直播<\/a>//g' $line;
   sed -i 's/<a href="http:\/\/m.tvyan.com\/zuqiubifen\/">足球比分<\/a>//g' $line;
done
