from src.Class.PackageManagement import PackageManagement
from src.setup import chaotic_aur, mirrorlist, pacman_conf
from src.i3wm import install_i3wm, systemctl_config, essential_build, install_fonts, copy_scripts
from src.drivers import install_driver
from src.software import dev_software, current_software, flatpak
from custom import wallpapers, config

def main():
    # setup.py
    chaotic_aur()

    loc_aur: str = ""
    while (loc_aur != "yay" and loc_aur != "paru"):
        loc_aur = input("You want to install yay or paru? (yay/paru): ")

    Pm = PackageManagement(aur=loc_aur)

    Pm.install(Pm.aur)
    mirrorlist()
    pacman_conf()


    # i3wm.py
    install_i3wm(Pm)
    systemctl_config(Pm)
    essential_build(Pm)
    install_fonts(Pm)
    copy_scripts()


    # Drivers.py
    install_driver(Pm)


    # software.py
    dev_software(Pm)
    current_software(Pm)
    flatpak(Pm)


    # Final
    wallpapers()
    config()
    


if __name__ == "__main__":
    main()
