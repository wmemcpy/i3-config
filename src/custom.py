from src.Class.PackageManagement import PackageManagement


def wallpapers(Pm: PackageManagement):
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp11834730.jpg https://wallpapercave.com/wp/wp11843903.jpg https://wallpapercave.com/wp/wp3087334.jpg", "Downloading wallpaper Spiderman")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp6391301.png https://wallpapercave.com/wp/wp5946817.png https://wallpapercave.com/wp/wp1812237.jpg", "Downloading wallpaper Gravity Falls")


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
