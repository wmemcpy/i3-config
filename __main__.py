#!/usr/bin/env python3

from src.Class.PackageManagement import PackageManagement
from src.setup import mirrorlist, pacman_conf
from src.i3wm import install_i3wm, systemctl_config, essential_build, install_fonts
from src.drivers import install_driver
from src.software import dev_software, current_software, flatpak
from src.custom import wallpapers, vscode, config, flatpak_themes
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

    Pm.command("sudo pacman -S --noconfirm --needed git base-devel",
               "Installing git and base-devel")
    if Pm.aur == "paru":
        Pm.command("git clone https://aur.archlinux.org/paru.git",
                   "Cloning paru")
        Pm.command("cd paru && makepkg -si --noconfirm && cd ..",
                   "Installing paru")
    else:
        Pm.command(
            "git clone https://aur.archlinux.org/yay-bin.git", "Cloning yay")
        Pm.command("cd yay-bin && makepkg -si --noconfirm && cd ..",
                   "Installing yay")

    mirrorlist(Pm)
    pacman_conf(Pm)

    install_i3wm(Pm)
    systemctl_config(Pm)
    essential_build(Pm)
    install_fonts(Pm)

    Pm.command("mkdir -p ~/.scripts", "Creating ~/.scripts")
    Pm.copy_file("scripts/*", "~/.scripts/",
                 log_msg="Copying scripts to ~/.scripts")

    install_driver(Pm)

    dev_software(Pm)
    current_software(Pm)
    flatpak(Pm)

    wallpapers(Pm)
    vscode(Pm)
    config(Pm)
    flatpak_themes(Pm)

    end_time = time()
    elapsed_time = end_time - start_time

    print("\n-----------------------------------------------------")
    print(f"Finished in {elapsed_time} seconds!")
    print("-----------------------------------------------------")


if __name__ == "__main__":
    main()
