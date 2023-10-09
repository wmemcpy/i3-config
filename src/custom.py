from System import System

def wallpaper():
    # Create directory Wallpaper in Images folder
    import os
    os.mkdir("~/Images/Wallpaper")
    # Download wallpaper
    System.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12875568.jpg https://wallpapercave.com/uwp/uwp3653361.jpeg https://wallpapercave.com/wp/wp3858321.jpg https://wallpapercave.com/wp/wp11831379.jpg https://wallpapercave.com/wp/wp11831382.jpg", "Downloading wallpaper MHA")
    System.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp11971220.jpg https://wallpapercave.com/wp/wp12319926.jpg https://wallpapercave.com/wp/wp11846249.jpg https://wallpapercave.com/wp/wp12319954.jpg https://wallpapercave.com/wp/wp11971284.jpg", "Downloading wallpaper Spiderman")
    System.command("wget -P ~/Images/Wallpaper https://wallpapercave.com/wp/wp12301210.jpg https://wallpapercave.com/wp/wp12099472.jpg https://wallpapercave.com/wp/wp12301247.jpg", "Downloading wallpaper Gravity Falls")
