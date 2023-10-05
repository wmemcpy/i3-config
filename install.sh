#!/usr/bin/env bash

# abort on errors
set -e

if [ "$EUID" -ne 0 ]
    then echo "Please run as root"
    exit 1
fi

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/src/log.sh"
source "$DIR/src/setup.sh"
source "$DIR/src/install_lst.sh"
source "$DIR/src/screens.sh"

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
