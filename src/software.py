from src.Class.PackageManagement import PackageManagement



def dev_software(Pm: PackageManagement):
    Pm.install_lst([
        'visual-studio-code-bin',
        'gdb',
        'valgrind',
        'clang',
        'gcc',
        'cmake',
        'make',
        'rust',
        'zig',
        'go',
        'jdk8-openjdk',
        'jdk17-openjdk'
    ])

    Pm.copy_file("config/Code/settings.json", "~/.config/Code/User/settings.json",
                 log_msg="Copying settings.json to Code")


def current_software(Pm: PackageManagement):
    Pm.install_lst([
        'spotify-launcher',
        'discord',
        'firefox',
        'slack-desktop',
        'glava',
    ])

    Pm.command("glava --copy-config", "Copying glava config")

    # Minecraft
    Pm.install_lst([
        'prismlauncher-qt5-bin',
        'prismlauncher-themes-git',
    ])


def flatpak(Pm: PackageManagement):
    Pm.install("flatpak")

    Pm.command("flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
               "Adding flathub repo")

    Pm.install_lst([
        'com.github.tchx84.Flatseal',
        'io.github.giantpinkrobots.flatsweep',
        'com.valvesoftware.Steam',
        'net.lutris.Lutris',
        'com.heroicgameslauncher.hgl'
    ], flatpak=True)
