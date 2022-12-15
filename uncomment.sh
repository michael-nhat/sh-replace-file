#!/bin/bash
if ! grep -q '<!-- <a href="http://n.mamadebaobao.com/shijiebei/">世界杯</a>' "$1"; then
echo "no comment: $1";
else
echo "commented: $1";
  sed -i 's/<!-- <a href="http:\/\/n.mamadebaobao.com\/shijiebei\/">世界杯<\/a> -->/<a href="http:\/\/n.mamadebaobao.com\/shijiebei\/">世界杯<\/a>/g' $1 ;
fi
