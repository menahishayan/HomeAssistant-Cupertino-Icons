import re
from os import listdir
from os.path import isfile, join
from xml.dom import minidom

path = './Icons/v3/Extracted2/'
files = [f for f in listdir(path) if f.endswith('.svg') and not f.startswith('.')]

for name in files: 
    try:
        src = minidom.parse(path + name)

        resizedSVG = minidom.parse('./Icons/v3/Full Color/' + name)

        for p1,p2 in zip(src.getElementsByTagName('path'), resizedSVG.getElementsByTagName('path')):
            if p1.hasAttribute("class"):
                classString = p1.getAttribute("class")
                p2.setAttribute("class",classString)
                classList = classString.split(' ')
                if 'SFSymbolsPreview' in classList[-1]:
                    color = classList[-1].split('SFSymbolsPreview')[1]
                    p2.setAttribute("style","fill: #{};".format(color))

        dest = open('./Icons/v3/Full Color/' + name, "w")
        resizedSVG.writexml(dest)
    except Exception as e:
        print(e)

