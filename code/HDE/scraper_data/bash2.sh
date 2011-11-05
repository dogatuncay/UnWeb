#!/bin/sh

python /home/doga/Desktop/scraper_data/db_urlto_notepad4.py

java -cp scrape.jar Scrape.Main URL.txt OUT.csv

python /home/doga/Desktop/scraper_data/update_indexed5.py



