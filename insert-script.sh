#!/bin/awk -f
BEGIN {
    FS=""
}  
{
   for(i=1;i<=NF;i++)
     { if($i=="|"){ p=i } }
}
END{  print p }