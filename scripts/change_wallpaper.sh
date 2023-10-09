#!/bin/bash

WALLPAPER_DIR=~/Images/Wallpaper

SLEEP_TIME=60

if [ ! -d "$WALLPAPER_DIR" ]; then
    echo "Le dossier $WALLPAPER_DIR n'existe pas."
    exit 1
fi

while true; do
    RANDOM_WALLPAPER=$(find "$WALLPAPER_DIR" -type f | shuf -n 1)
    
    nitrogen --set-zoom-fill "$RANDOM_WALLPAPER"
    
    sleep "$SLEEP_TIME"
done
