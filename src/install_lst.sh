DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "$DIR/src/log.sh"

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

    # Read the file line by line
    while IFS= read -r line
    do
        # Skip empty lines
        if [ -z "$line" ]
        then
            continue
        fi

        # Skip comments
        if [[ "$line" =~ ^#.* ]]
        then
            continue
        fi

        # Install the package
        echo_log "installing $line"
        $1 -S --noconfirm --needed "$line"
    done < "$2"
}
