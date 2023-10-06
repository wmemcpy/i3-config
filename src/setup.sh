#!/usr/bin/env bash

source "src/utils.sh"

# This function creates a directory for scripts and copies scripts from a data directory to the newly created directory.
function configure_script {
    echo_log "creating scripts directory"
    mkdir -p ~/.scripts
    echo_log "copying scripts"
    cp data/scripts/* ~/.scripts
}

export -f configure_script

# This function configures the bashrc file by moving any existing bashrc file to a backup location and copying a new bashrc file to the home directory.
# If a bashrc file already exists, it will be moved to a backup location before the new file is copied.
function configure_bash {
    if [ -f ~/.bashrc ]; then
        echo_log "moving existing bashrc to backup"
        mv ~/.bashrc ~/.bashrc.bak
    fi
    echo_log "copying bashrc"
    cp data/.bashrc ~/.bashrc
}

export -f configure_bash

# Configures i3 window manager by copying the i3 config and bar config files to the appropriate directories.
# If the config files already exist, they are backed up before being replaced.
function configure_i3wm {
    # Copy i3 config
    echo_log "creating i3wm config directory"

    local config_path=".config/i3/config"

    echo_log "creating i3wm config directory"
    mkdir -p ~/.config/i3
    if [ -f $config ]; then
        echo_log "moving existing i3wm config to backup"
        mv $config_path $config_path.bak
    fi 
    echo_log "copying i3wm config"
    cp data/i3wm/config $config_path

    local status_path="/etc/i3status.conf"

    # Copy bar config
    if [ -f $status_path ]; then
        echo_log "moving existing i3status config to backup"
        sudo mv $status_path $status_path.bak
    fi
    echo_log "copying i3status config"
    sudo cp data/i3wm/i3status.conf $status_path
}

export -f configure_i3wm
