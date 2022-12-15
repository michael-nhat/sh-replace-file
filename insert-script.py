#!/usr/bin/python
import sys;

fileInName = sys.argv[1]
fileIn = open(fileInName, "rw")
strIn = fileIn.read()

searchStr = "</script>"
startPos = strIn.rfind(searchStr)
if (startPos > 0):
        
    chunk = strIn[startPos: startPos + 9]
    targetPos = startPos + len(searchStr)
    strInsert = '''

    <script>
    var _hmt = _hmt || [];
    (function() {
    var hm = document.createElement("script");
    hm.src = "https://hm.baidu.com/hm.js?a87ff42a01e584a69e3421eecad7cb31";
    var s = document.getElementsByTagName("script")[0]; 
    s.parentNode.insertBefore(hm, s);
    })();
    </script>

    '''
    resultStr = strIn[:targetPos] + strInsert + strIn[targetPos:]
    # print resultStr
    fileIn.write(resultStr)
else:
    print "no script"

fileIn.close()