#!/usr/bin/env bash

function init_log_file {
    if [ ! -d "../log" ]; then
        mkdir ../log
    fi

    local nb_log_file=$(ls ../log/ | wc -l) + 1
    local log_file="../log/log_$nb_log_file.txt"

    if [ ! -f "$log_file" ]; then
        touch "$log_file"
    fi

    echo "$log_file"
}

function echo_log {
    local log_msg="[`date '+%Y-%m-%d %H:%M:%S'`]: $1"
    local log_file=$(init_log_file)

    echo "$log_msg" >> "$log_file"
    echo "$log_msg"
}
