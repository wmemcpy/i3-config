#!/usr/bin/env bash

# abort on errors
set -e

if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for file in "$DIR/src/"*.sh
do
    source "$file"
done

function main {
    install_dependencies
    install_yay
    install_i3wm

    configure_script
    configure_bash
    configure_i3wm

    script_screen_generate

    if [ "$1" == "-fr" ]; then
        setxkbmap fr
    fi
}

echo "Do you want to install the script? (y/n)"
read answer

if [ "$answer" != "${answer#[Yy]}" ] ;then
    main $1
fi
