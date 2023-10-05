#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/install.sh"

LOG_FILE=""

function init_log_file {
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
