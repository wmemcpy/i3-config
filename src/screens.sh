
# This function generates a script that sets the maximum resolution and refresh rate for each connected display using xrandr.
# The script is saved to $HOME/.scripts/screens.sh
function script_screen_generate() {
    mkdir -p $HOME/.scripts

    if [ -f $HOME/.scripts/screens.sh ]; then
        rm $HOME/.scripts/screens.sh
    fi
    touch $HOME/.scripts/screens.sh

    echo "#!/usr/bin/env bash" >> $HOME/.scripts/screens.sh
    local displays=$(xrandr | grep " connected" | awk '{print $1}')

    for display in $displays
    do
        local line_res_max=$(xrandr --query | grep $display -A10 | grep "   " | sort -r -k4 -t"x" | head -n1)
        local max_res=$(echo $line_res_max | awk '{print $1}')
        local available_rates=$(echo $line_res_max | awk '{$1=""; print $0}' | grep -oP "[0-9]+(\.[0-9]+)?(?=\*)?")
        local rate_max=$(echo $available_rates | tr " " "\n" | sort -n -r | head -n1) 

        echo "xrandr --output $display --mode $max_res --rate $rate_max" >> $HOME/.scripts/screens.sh
    done
}
