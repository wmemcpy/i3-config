from Class.System import System
from os import mkdir

def wallpapers():
    mkdir("~/Images/Wallpaper")

    sys = System()

    sys.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12875568.jpg https://wallpapercave.com/uwp/uwp3653361.jpeg https://wallpapercave.com/wp/wp3858321.jpg https://wallpapercave.com/wp/wp11831379.jpg https://wallpapercave.com/wp/wp11831382.jpg", "Downloading wallpaper MHA")
    sys.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp11971220.jpg https://wallpapercave.com/wp/wp12319926.jpg https://wallpapercave.com/wp/wp11846249.jpg https://wallpapercave.com/wp/wp12319954.jpg https://wallpapercave.com/wp/wp11971284.jpg", "Downloading wallpaper Spiderman")
    sys.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12301210.jpg https://wallpapercave.com/wp/wp12099472.jpg https://wallpapercave.com/wp/wp12301247.jpg", "Downloading wallpaper Gravity Falls")

def config():
    sys = System()
    
    # i3 
    sys.copy_file("~/.config/i3/config", "~/.config/i3/config.bak")
    sys.copy_file("../config/i3/config", "~/.config/i3/config")

    # i3status
    sys.copy_file("/etc/i3status.conf", "/etc/i3status.conf.bak")
    sys.copy_file("../config/i3/i3status.conf", "/etc/i3status.conf")

    # Kitty
    sys.copy_file("~/.config/kitty/kitty.conf", "~/.config/kitty/kitty.conf.bak")
    sys.copy_file("../config/kitty/kitty.conf", "~/.config/kitty/kitty.conf")
