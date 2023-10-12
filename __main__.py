#!/usr/bin/env python3

from src.Class.PackageManagement import PackageManagement
from src.setup import mirrorlist, pacman_conf
from src.i3wm import install_i3wm, systemctl_config, essential_build, install_fonts
from src.drivers import install_driver
from src.software import dev_software, current_software, flatpak
from src.custom import wallpapers, config
from time import time
from os import system

def print_welcome_message():
    system('clear')
    welcome_message = r"""
 █████  ████████                                     ██████   ███          
░░███  ███░░░░███                                   ███░░███ ░░░           
 ░███ ░░░    ░███     ██████   ██████  ████████    ░███ ░░░  ████   ███████
 ░███    ██████░     ███░░███ ███░░███░░███░░███  ███████   ░░███  ███░░███
 ░███   ░░░░░░███   ░███ ░░░ ░███ ░███ ░███ ░███ ░░░███░     ░███ ░███ ░███
 ░███  ███   ░███   ░███  ███░███ ░███ ░███ ░███   ░███      ░███ ░███ ░███
 █████░░████████    ░░██████ ░░██████  ████ █████  █████     █████░░███████
░░░░░  ░░░░░░░░      ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░     ░░░░░  ░░░░░███
                                                                   ███ ░███
                                                                  ░░██████ 
                                                                   ░░░░░░  
    """
    print(welcome_message)
    print("Welcome to the setup script!")
    print("This process might take a while. Sit back and relax.")
    print("-----------------------------------------------------\n")

def main():
    start_time = time()

    print_welcome_message()

    Pm = PackageManagement()

    # Install yay or paru    
    loc_aur: str = ""
    while (loc_aur != "yay" and loc_aur != "paru"):
        loc_aur = input("You want to install yay or paru? (yay/paru): ")
    Pm.aur = loc_aur

    Pm.command("sudo pacman -S --noconfirm --needed git base-devel", "Installing git and base-devel")
    if Pm.aur == "paru":
        Pm.command("git clone https://aur.archlinux.org/paru.git", "Cloning paru")
        Pm.command("cd paru && makepkg -si --noconfirm && cd ..", "Installing paru")
    else:
        Pm.command("git clone https://aur.archlinux.org/yay-bin.git", "Cloning yay")
        Pm.command("cd yay-bin && makepkg -si --noconfirm && cd ..", "Installing yay")

    mirrorlist(Pm)
    pacman_conf(Pm)

    install_i3wm(Pm)
    systemctl_config(Pm)
    essential_build(Pm)
    install_fonts(Pm)

    Pm.copy_file("scripts/*", "~/.scripts", log_msg="Copying scripts to ~/.scripts")

    install_driver(Pm)

    dev_software(Pm)
    current_software(Pm)
    flatpak(Pm)

    wallpapers(Pm)
    config(Pm)

    end_time = time()
    elapsed_time = end_time - start_time

    print("\n-----------------------------------------------------")
    print("\033[1;32;40mSetup Complete!\033[0m")
    print(f"\033[1;34;40mTotal execution time: {elapsed_time:.2f} seconds.\033[0m")
    print("\033[1;33;40mReboot your system for all changes to take effect.\033[0m")
    print("\033[1;35;40mThank you for using the script! Have a great day ❤ !\033[0m\n")


if __name__ == "__main__":
    main()
