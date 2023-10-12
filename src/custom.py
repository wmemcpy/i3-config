from src.Class.PackageManagement import PackageManagement


def wallpapers(Pm: PackageManagement):
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12875568.jpg https://wallpapercave.com/uwp/uwp3653361.jpeg https://wallpapercave.com/wp/wp3858321.jpg https://wallpapercave.com/wp/wp11831379.jpg https://wallpapercave.com/wp/wp11831382.jpg", "Downloading wallpaper MHA")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp11971220.jpg https://wallpapercave.com/wp/wp12319926.jpg https://wallpapercave.com/wp/wp11846249.jpg https://wallpapercave.com/wp/wp12319954.jpg https://wallpapercave.com/wp/wp11971284.jpg", "Downloading wallpaper Spiderman")
    Pm.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12301210.jpg https://wallpapercave.com/wp/wp12099472.jpg https://wallpapercave.com/wp/wp12301247.jpg",
               "Downloading wallpaper Gravity Falls")


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
