#
# ~/.bashrc
#

# Sortir si le shell n'est pas interactif
[[ $- != *i* ]] && return

# Configuration de MANPAGER pour une meilleure lisibilité avec bat
export MANROFFOPT="-c"
export MANPAGER="sh -c 'col -bx | bat -l man -p'"

# Alias pour colorer et formater la sortie de ls et grep
alias ls='ls --color=auto -F --group-directories-first'
alias ll='ls --color=auto -lF --group-directories-first'
alias la='ls --color=auto -aF --group-directories-first'
alias l='ls --color=auto -CF --group-directories-first'
alias grep='grep --color=auto'

# Couleurs pour l'invite
YELLOW="\[\033[1;33m\]"
RED="\[\033[1;31m\]"
RESET="\[\033[0m\]"

# Fonction pour analyser la branche git actuelle et son statut
parse_git_branch() {
    BRANCH=$(git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/')
    
    if [[ -n "$BRANCH" ]]; then
        GIT_STATUS=$(git for-each-ref --format '%(upstream:track)' "$(git symbolic-ref -q HEAD)" 2> /dev/null)
        NUM_AHEAD=$(echo " $GIT_STATUS " | grep ahead | sed 's/.*ahead \([0-9]*\).*/\1/')
        NUM_BEHIND=$(echo " $GIT_STATUS " | grep behind | sed 's/.*behind \([0-9]*\).*/\1/')
        AHEAD=""
        BEHIND=""
        
        [[ -n "$NUM_AHEAD" ]] && AHEAD="↑$NUM_AHEAD"
        [[ -n "$NUM_BEHIND" ]] && BEHIND="↓$NUM_BEHIND"
        
        echo " ($BRANCH$AHEAD$BEHIND)"
    fi
}

# Fonction pour construire l'invite PS1
prompt_command() {
    local exit_code=$?
    local signal_name=""
    
    if [[ $exit_code -ne 0 ]]; then
        if [[ $exit_code -gt 128 ]]; then
            signal_name=$(kill -l $exit_code 2>/dev/null)
            [[ -n $signal_name ]] && PS1="\w${YELLOW}\$(parse_git_branch) ${RED}(SIG${signal_name})${RESET} $ " || PS1="\w${YELLOW}\$(parse_git_branch) ${RED}(${exit_code})${RESET} $ "
        else
            PS1="\w${YELLOW}\$(parse_git_branch)${RESET} ${RED}($exit_code)${RESET} $ "
        fi
    else
        PS1="\w${YELLOW}\$(parse_git_branch)${RESET} $ "
    fi
}

# Définir la commande de prompt
PROMPT_COMMAND=prompt_command
