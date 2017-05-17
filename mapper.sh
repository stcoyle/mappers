#!/bin/bash

#automation of WALDO map.


#go to the data directory called test
cd /test

#delete old data
echo removing old files ...
python deleteXLSX.py


#open ftp client
filezilla &&
#pause to retrive new files from ftp site (work on automation)
read -p "Download new files and then press enter"


#extract data from files and make map_data.csv in /home/map_data
echo creating new map_data.csv
python multi.py


#change directory to /root/Desktop
cd /root/Desktop

#run waldo script to make map
echo creating new players_heatmap.html
python Waldo.py

#open players_heatmap.html to modify
echo change threshold in html to 50
echo change radius to 20
echo change opacity to 1.600000
kwrite /usr/share/nginx/html/players_heatmap.html
firefox 10.1.10.100/players_heatmap.html