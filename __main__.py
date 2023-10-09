from PackageManagement import PackageManagement
from src.i3wm import install_i3wm, systemctl_config, essential_build, install_fonts
from src.software import dev_software
from src.Pm import chaotic_aur, mirrorlist

def main():
    # src.Pm
    chaotic_aur()
    mirrorlist()

    # src.i3wm
    Pm = PackageManagement()
    install_i3wm(Pm)
    systemctl_config(Pm)
    essential_build(Pm)
    install_fonts(Pm)

    # src.software
    dev_software(Pm)

    

if __name__ == "__main__":
    main()
