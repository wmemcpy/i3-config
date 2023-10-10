from Class.PackageManagement import PackageManagement
from Class.System import System

def install_i3wm(Pm: PackageManagement) -> bool:
    Pm.install_lst([
		'i3-wm',
		'i3lock-color',
		'i3status',
		'i3blocks',
		'kitty',
		'lightdm-gtk-greeter',
		'lightdm',
		'rofi'
        'xdg-'
    ])

def systemctl_config(Pm: PackageManagement) -> bool:
    Pm.command("sudo systemctl enable lightdm", "Enabling lightdm")
    Pm.command("sudo systemctl start lightdm.service", "Starting lightdm")

    Pm.command("sudo systemctl enable NetworkManager", "Enabling NetworkManager")
    Pm.command("sudo systemctl start NetworkManager", "Starting NetworkManager")

def essential_build(Pm: PackageManagement) -> bool:
    Pm.install_lst([
        'git',
        'base-devel',
        'unzip',
        'zip',
        'xorg-xrandr',
        'feh',
        'redshift',
        'picom',
        'polkit'
        'polkit-gnome',
        'vim',
        'viewnior',
        'bat',
        'maim',
        'xclip',
        'nitrogen',
        'fastfetch',
        'imagemagick',
    ])

def install_fonts(Pm: PackageManagement) -> bool:
    Pm.install_lst([
        'gnu-free-fonts',
        'ttf-roboto-mono',
        'ttf-font-awesome',
        'noto-fonts',
        'ttf-joypixels',
        'ttf-dejavu',
        'ttf-liberation',
        'ttf-inconsolata',
        'ttf-hack',
        'ttf-fira-code',
        'ttf-jetbrains-mono-nerd',
        'ttf-mononoki-nerd',
        'ttf-cascadia-code-nerd',
        'ttf-material-design-icons-extended',
        'noto-fonts-emoji-flags',
        'ttf-maple'
    ])

def copy_scripts():
    System.copy_file("../scripts/*", '~/scripts')
