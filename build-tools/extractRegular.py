import re
from os import listdir
from os.path import isfile, join
from xml.dom import minidom

# dest = open("HomeAssistant-Cupertino-Icons.js", "w")
# dest.write('const CUPERTINO_ICONS_MAP = {')

path = './Icons/v2/Original/'
files = [f for f in listdir(path) if f.endswith('.svg') and not f.startswith('.')]

for name in files: 
    try:
        src = minidom.parse(path + name)

        dest = open("./Icons/v2/Extracted/" + name, "w")
        pathString = ""

        for g in src.getElementsByTagName('g'):
            if g.getAttribute('id') == 'Regular-M':
                pathString = g.getElementsByTagName('path')[0].getAttribute('d')
        dest.write(
            '<?xml version="1.0" encoding="utf-8"?><!-- Generator: Adobe Illustrator 22.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  --><svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" \
                height="100px" width="100px"><path d="{}"/></svg>'.format(pathString)
            )
    except:
        print(name)

# dest.write('};async function getIcon(n){return{path:CUPERTINO_ICONS_MAP[n]}}if(window.customIconsets=window.customIconsets||{},window.customIconsets.ios=getIcon,!window.frontendVersion||window.frontendVersion<20200519){const n=document.createElement("ha-iconset-svg");n.name="ios",n.size="24";let o="";for(let n in CUPERTINO_ICONS_MAP)o+=`<g id="${n}"><path d="${CUPERTINO_ICONS_MAP[n]}" /></g>`;n.innerHTML=`<svg><defs>${o}</defs></svg>`,document.body.appendChild(n)}')
