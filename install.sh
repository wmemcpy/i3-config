#!/usr/bin/env bash

sudo -v -p "Please enter your sudo password: "

set -e

if [ "$1" == "-v" ] || [ "$1" == "--verbose" ]; then
    set -x
fi

source "src/install.sh"
source "src/screens.sh"
source "src/setup.sh"

function main {
    init_log_file
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
