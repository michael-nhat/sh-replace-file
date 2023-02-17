#!/usr/bin/python
import sys;
import re;

# input file must have 2  baidu-script tag
fileInName = sys.argv[1]
with open(fileInName, 'r+') as fileIn:
    strIn = fileIn.read()
    regexStart = r"<script>\s*var _hmt ="
    regexEnd = r"insertBefore\(hm, s\);\s*\}\)\(\);\s*</script>"

    r1 = re.findall(regexStart, strIn)
    r2 = re.findall(regexEnd, strIn)
    if (len(r1) > 1 and len(r2) > 1):
        firstPosStr = r1[0]
        secondPosStr = r2[0]

        firstPos = strIn.find(firstPosStr);
        secondPos = strIn.find(secondPosStr) + len(secondPosStr);
        resultStr = strIn[:firstPos - 1] + strIn[secondPos+1:]
        # print resultStr
        fileIn.seek(0)
        fileIn.write(resultStr)
        fileIn.truncate()
    else:
        print "script repeat but commented"

    fileIn.close()
