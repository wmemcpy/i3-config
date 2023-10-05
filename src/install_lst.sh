#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/log.sh"

#
# This function installs a list of packages from a file using a specified package manager.
# The function takes two arguments:
#   - package_manager: the name of the package manager to use (e.g. "apt", "pacman")
#   - file: the path to the file containing the list of packages to install
#
# If the number of arguments is not 2, the function prints an error message and exits with status 1.
# If the specified package manager is not installed, the function prints an error message and exits with status 2.
# If the specified file does not exist, the function prints an error message and exits with status 3.
#
# The function reads each line of the file and installs the corresponding package using the specified package manager.
# If a line is empty or starts with a "#" (comment), it is skipped.
# The function logs each package installation using the echo_log function.
# If the specified package manager is "pacman", the function runs the installation command with sudo.
#
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
