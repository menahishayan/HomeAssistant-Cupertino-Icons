import re
from os import listdir
from os.path import isfile, join
from xml.dom import minidom

# dest = open("HomeAssistant-Cupertino-Icons.js", "w")
# dest.write('const CUPERTINO_ICONS_MAP = {')

path = './Icons/v3/Original/'
files = [f for f in listdir(path) if f.endswith('.svg') and not f.startswith('.')]

for name in files: 
    try:
        src = minidom.parse(path + name)

        dest = open("./Icons/v3/Extracted2/" + name.replace('.','-').replace('-svg','.svg'), "w")
        pathString = ""

        for g in src.getElementsByTagName('g'):
            if g.getAttribute('id') == 'Regular-M':
                for p in g.getElementsByTagName('path'):
                    pathString += p.toxml() #SFSymbolsPreviewFFFFFF
        dest.write(
            '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" \
                height="1024px" width="1024px">{}</svg>'.format(pathString)
            )
    except Exception as e:
        print(e)

# dest.write('};async function getIcon(n){return{path:CUPERTINO_ICONS_MAP[n]}}if(window.customIconsets=window.customIconsets||{},window.customIconsets.ios=getIcon,!window.frontendVersion||window.frontendVersion<20200519){const n=document.createElement("ha-iconset-svg");n.name="ios",n.size="24";let o="";for(let n in CUPERTINO_ICONS_MAP)o+=`<g id="${n}"><path d="${CUPERTINO_ICONS_MAP[n]}" /></g>`;n.innerHTML=`<svg><defs>${o}</defs></svg>`,document.body.appendChild(n)}')
