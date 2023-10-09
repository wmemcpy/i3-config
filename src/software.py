from System import System
from PackageManagement import PackageManagement

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
