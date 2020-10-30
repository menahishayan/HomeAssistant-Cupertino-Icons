#!/bin/bash

brew install fontforge
fontforge -lang=ff -c 'Open($1); SelectWorthOutputting(); foreach Export("svg"); endloop;' CupertinoIcons.ttf 