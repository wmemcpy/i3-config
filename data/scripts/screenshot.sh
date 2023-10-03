#!/usr/bin/env bash

DIR=~/Pictures/Screenshots
mkdir -p "$DIR"

FILENAME="$DIR/Screenshot-$(date +%F-%T).png"

if [[ $1 == "select" ]]; then
    maim -s "$FILENAME"
else
    maim "$FILENAME"
fi

xclip -selection clipboard -t image/png -i "$FILENAME"
