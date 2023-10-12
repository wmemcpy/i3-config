from src.Class.PackageManagement import PackageManagement


def wallpapers(Pm: PackageManagement):
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/download/wakfu-wallpapers-wp1986515 https://wallpapercave.com/download/wakfu-wallpapers-wp1986665 https://wallpapercave.com/download/wakfu-wallpapers-wp1986676", "Downloading wallpaper Wakfu")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11834730 https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11834717 https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11839530 https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11834745 https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11459908 https://wallpapercave.com/download/spider-man-across-the-spider-verse-movie-wallpapers-wp11846249", "Downloading wallpaper Spiderman")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp6391301 https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp11430355 https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp11430366 https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp11430371 https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp11430374 https://wallpapercave.com/download/gravity-falls-laptop-wallpapers-wp11430378", "Downloading wallpaper Gravity Falls")


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
