#!/usr/bin/env bash

source "src/utils.sh"

# Installs git and base-devel dependencies and updates the system.
function install_dependencies {
    echo_log "installing git and base-devel"
    sudo pacman -S --noconfirm --needed git base-devel
    echo_log "updating system"
    sudo pacman -Syyuu --noconfirm
}

export -f install_dependencies

# Installs yay package manager if it's not already installed.
function install_yay {
    if ! command -v yay &> /dev/null
    then
        echo_log "cloning yay"
        git clone https://aur.archlinux.org/yay-bin.git
        cd yay-bin
        echo_log "building yay"
        makepkg -si --noconfirm
        cd ..
        rm -rf yay-bin
    else
        echo_log "yay already installed"
    fi
}

export -f install_yay

# Installs i3 window manager using yay package manager
function install_i3wm {
    install_lst yay "$DIR/data/i3wm/i3wm.lst"
}

export -f install_i3wm
