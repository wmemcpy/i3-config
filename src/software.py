from Class.System import System
from Class.PackageManagement import PackageManagement

def dev_software(Pm: PackageManagement):
    Pm.install_lst([
        'visual-studio-code-bin',
        'vim',
        'gdb',
        'valgrind',
        'clang',
        'gcc',
        'cmake',
        'make',
        'rust',
        'rustup',
        'zig',
        'go'
    ])

    System.copy_file("../config/Code/settings.json", "~/.config/Code/User/settings.json")

def current_software(Pm: PackageManagement):
    Pm.install_lst([
        'spotify-launcher',
        'discord',
        'firefox',
        'slack-desktop'
    ])


def flatpak(Pm: PackageManagement):
    Pm.install("flatpak")

    System.command("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo", "Adding flathub repo")

    Pm.faltapk_install("com.spotify.Client")
