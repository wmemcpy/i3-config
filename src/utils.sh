#!/usr/bin/env bash

LOG_FILE=""

function init_log_file {
    read -p "Do you want to log the installation? (y/n) " answer

    mkdir -p "${DIR}/../log"

    local nb_log_file=$(ls "${DIR}/../log/" | wc -l)
    local log_file="${DIR}/../log/log_$nb_log_file.txt"

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
    if [ $# -ne 2 ]
    then
        echo "Usage: install_lst.sh <package_manager> <file>"
        exit 1
    fi

    if ! command -v $1 &> /dev/null
    then
        echo "$1 is not installed"
        exit 2
    fi

    if [ ! -f "$2" ]
    then
        echo "File $2 does not exist"
        exit 3
    fi

    while IFS= read -r line
    do
        if [ -z "$line" ]
        then
            continue
        fi

        if [[ "$line" =~ ^#.* ]]
        then
            continue
        fi

        echo_log "installing $line"
        if [ "$1" == "pacman" ]
        then
            sudo $1 -S --noconfirm --needed $line
        else
            $1 -S --noconfirm --needed $line
        fi
    done < "$2"
}

export -f install_lst