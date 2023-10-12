from src.Class.PackageManagement import PackageManagement
from re import compile
from subprocess import run

# https://aur.chaotic.cx/


def chaotic_aur(Pm: PackageManagement) -> None:
    # Key ID
    key_id = "3056513887B78AEB"

    # Key server URL
    keyserver = "keyserver.ubuntu.com"

    # Package URLs
    pkg_keyring_url = "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst"
    pkg_mirrorlist_url = "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst"

    recv_key_cmd = f"sudo pacman-key --recv-key {key_id} --keyserver {keyserver}"
    lsign_key_cmd = f"sudo pacman-key --lsign-key {key_id}"
    update_pkg_cmd = f"sudo pacman -U '{pkg_keyring_url}' '{pkg_mirrorlist_url}' --noconfirm --needed"

    # Add repo
    lines_to_add = """
    [chaotic-aur]
    Include = /etc/pacman.d/chaotic-mirrorlist
    """

    file_path = "/etc/pacman.conf"

    # Read file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    new_lines = []

    # Check if repo already exists, if not add it
    if not any("[chaotic-aur]" in line for line in lines):
        for line in lines:
            new_lines.append(line)
            if line == lines[-1]:
                new_lines.append(lines_to_add)
    else:
        new_lines = lines

    # Write to temp file
    with open("temp_pacman.conf", 'w') as temp_file:
        temp_file.writelines(new_lines)

    Pm.copy_file("temp_pacman.conf", "/etc/pacman.conf",
                 sudo=True, log_msg="Adding chaotic-aur repo")

    # Delete temp file
    Pm.command("rm temp_pacman.conf", "Deleting temp file")
    # Add key
    Pm.command(recv_key_cmd, "Receiving key")
    Pm.command(lsign_key_cmd, "Signing key")
    Pm.command(update_pkg_cmd, "Updating package")


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
        compile(r"#Color"),
        compile(r"#CheckSpace"),
        compile(r"#VerbosePkgLists"),
        compile(r"#ParallelDownloads = 5"),
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
