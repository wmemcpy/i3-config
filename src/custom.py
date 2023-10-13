from src.Class.PackageManagement import PackageManagement


def wallpapers(Pm: PackageManagement):
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp11834730.jpg https://wallpapercave.com/wp/wp11843903.jpg https://wallpapercave.com/wp/wp3087334.jpg", "Downloading wallpaper Spiderman")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp6391301.png https://wallpapercave.com/wp/wp5946817.png https://wallpapercave.com/wp/wp1812237.jpg",
               "Downloading wallpaper Gravity Falls")


def vscode(Pm: PackageManagement):
    Pm.command("code --install-extension Catppuccin.catppuccin-vsc",
               "Installing catppuccin theme")
    Pm.command("code --install-extension thang-nm.catppuccin-perfect-icons",
               "Installing catppuccin icons")
    Pm.command("code --install-extension formulahendry.code-runner",
               "Installing code runner")
    Pm.command("code --install-extension ionutvmi.path-autocomplete",
               "Installing path autocomplete")
    Pm.command("code --install-extension ziglang.vscode-zig",
               "Installing zig language support")
    Pm.command("code --install-extension ms-python.python",
               "Installing python language support")
    Pm.command("code --install-extension EricSia.pythonsnippets3",
               "Installing python snippets")
    Pm.command("code --install-extension ms-vscode.cpptools",
               "Installing c++ language support")
    Pm.command("code --install-extension jeff-hykin.better-cpp-syntax",
               "Installing better c++ syntax")
    Pm.command("code --install-extension 1YiB.rust-bundle",
               "Installing rust language support")
    Pm.command("code --install-extension mhutchie.git-graph",
               "Installing git graph")
    Pm.command("code --install-extension 13xforever.language-x86-64-assembly",
               "Installing x86-64 assembly language support")
    Pm.command("code --install-extension ms-python.autopep8",
               "Installing autopep8")


def config(Pm: PackageManagement):
    # i3
    Pm.copy_file("config/i3/config", "~/.config/i3/config",
                 log_msg="Copying i3 config")

    # i3status
    Pm.copy_file("config/i3/i3status.conf", "/etc/i3status.conf",
                 sudo=True, log_msg="Copying i3status.conf")

    # Kitty
    Pm.copy_file("config/kitty/kitty.conf",
                 "~/.config/kitty/kitty.conf", log_msg="Copying kitty.conf")

    # Rofi
    Pm.copy_file("config/rofi/config.rasi",
                 "~/.config/rofi/config.rasi", log_msg="Copying rofi config")


def flatpak_themes(Pm: PackageManagement):
    Pm.command("sudo flatpak override --filesystem=$HOME/.themes",
               "Flatpak override for themes")
    Pm.command("sudo flatpak override --filesystem=$HOME/.icons",
               "Flatpak override for icons")

    Pm.install_lst([
        'catppuccin-cursors-mocha',
        'catppuccino-gtk-theme',
    ])

def global_themes(Pm: PackageManagement):
    Pm.install_lst([
        'papirus-icon-theme',
    ])
    
    # Install themes
    Pm.command_with_enter('_prism-theme-installer', 'Specify the directory where you want to install themes')

    Pm.copy_file("config/.gtkrc-2.0", "~/.gtkrc-2.0", log_msg="Copying .gtkrc-2.0")
    Pm.copy_file("config/gtk-3.0/settings.ini", "~/.config/gtk-3.0/settings.ini", log_msg="Copying gtk-3.0 settings.ini")
    Pm.copy_file("config/gtk-4.0/settings.ini", "~/.config/gtk-4.0/settings.ini", log_msg="Copying gtk-4.0 settings.ini")