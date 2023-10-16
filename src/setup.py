from src.Class.PackageManagement import PackageManagement
from re import compile


def mirrorlist(Pm: PackageManagement) -> None:
    # Install reflector
    Pm.install("reflector")
    # Update mirrorlist
    Pm.command("sudo reflector --verbose --score 20 --fastest 5 --sort rate --save /etc/pacman.d/mirrorlist", "Updating mirrorlist")
    Pm.update_mirror()


def pacman_conf(Pm: PackageManagement) -> None:
    file_path: str = "/etc/pacman.conf"

    with open(file_path, 'r') as file:
        lines = file.readlines()

    patterns = [
        # Pacman options
        compile(r"#Color"),
        compile(r"#CheckSpace"),
        compile(r"#VerbosePkgLists"),
        compile(r"#ParallelDownloads = 5"),
        
        # Add multilib
        compile(r"#\[multilib\]"),
        compile(r"#Include = /etc/pacman.d/mirrorlist"),
    ]

    new_lines = []
    for line in lines:
        if any(pattern.match(line) for pattern in patterns):
            new_lines.append(line.lstrip('#').lstrip())
            if compile(r"#ParallelDownloads = 5").match(line):
                new_lines.append("ILoveCandy\n")
        else:
            new_lines.append(line)

    with open("temp_pacman.conf", 'w') as temp_file:
        temp_file.writelines(new_lines)

    Pm.copy_file("temp_pacman.conf", "/etc/pacman.conf",
                 sudo=True, log_msg="Updating pacman.conf")
