import re
from os import listdir
from os.path import isfile, join
from xml.dom import minidom

dest = open("HomeAssistant-Cupertino-Icons.js", "w")
dest.write('const CUPERTINO_ICONS_MAP = {')

path = './Icons/v2/Extracted/'
files = [f for f in listdir(path) if f.endswith('.svg') and not f.startswith('.')]

for name in files: 
    try:
        src = minidom.parse(path + name)

        path_strings = [path.getAttribute('d') for path in src.getElementsByTagName('path')]

        dest.write('\'{}\':\'{}\','.format(name.split('.')[0].replace('_','-'), path_strings[0]))
    except:
        print(name)

dest.write('};async function getIcon(n){return{path:CUPERTINO_ICONS_MAP[n]}}if(window.customIconsets=window.customIconsets||{},window.customIconsets.ios=getIcon,!window.frontendVersion||window.frontendVersion<20200519){const n=document.createElement("ha-iconset-svg");n.name="ios",n.size="24";let o="";for(let n in CUPERTINO_ICONS_MAP)o+=`<g id="${n}"><path d="${CUPERTINO_ICONS_MAP[n]}" /></g>`;n.innerHTML=`<svg><defs>${o}</defs></svg>`,document.body.appendChild(n)}')
