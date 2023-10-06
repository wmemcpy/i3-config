#!/usr/bin/env bash

LOG_FILE=""

function init_log_file {
    mkdir -p "../log"

    local log_file="../log/log.txt"

    if [ ! -f "$log_file" ]; then
        touch "$log_file"
    fi

    LOG_FILE="$log_file"
}

export -f init_log_file

function echo_log {
    local log_msg="[`date '+%Y-%m-%d %H:%M:%S'`]: $1"

    echo "$log_msg" >> "$LOG_FILE"
    echo "$log_msg"
}

export -f echo_log

function install_lst {
    if [ $# -ne 2 ]; then
        echo_log "Usage: install_lst.sh <package_manager> <file>"
        exit 1
    fi

    if ! command -v $1 &> /dev/null; then
        echo_log "$1 is not installed"
        exit 2
    fi

    if [ ! -f "$2" ]; then
        echo_log "File $2 does not exist"
        exit 3
    fi

    while IFS= read -r line
    do
        if [ -z "$line" ]; then
            continue
        fi

        if [[ "$line" =~ ^#.* ]]; then
            continue
        fi

        echo_log "installing $line"
        if [ "$1" == "pacman" ]; then
            sudo $1 -S --noconfirm --needed $line 2>&1
        else
            $1 -S --noconfirm --needed $line 2>&1
        fi
    done < "$2"
}

export -f install_lst