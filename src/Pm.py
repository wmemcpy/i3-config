from System import System
from PackageManagement import PackageManagement

# https://aur.chaotic.cx/
def chaotic_aur():
    # Key ID
    key_id = "3056513887B78AEB"

    # Key server URL
    keyserver = "keyserver.ubuntu.com"

    # Package URLs
    pkg_keyring_url = "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst"
    pkg_mirrorlist_url = "https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst"

    recv_key_cmd = f"pacman-key --recv-key {key_id} --keyserver {keyserver}"
    lsign_key_cmd = f"pacman-key --lsign-key {key_id}"
    update_pkg_cmd = f"pacman -U '{pkg_keyring_url}' '{pkg_mirrorlist_url}'"


    # Add repo
    lines_to_add = """
    [chaotic-aur]
    Include = /etc/pacman.d/chaotic-mirrorlist
    """
    pacman_conf_path = "/etc/pacman.conf"

    try:
        with open(pacman_conf_path, 'a') as file:
            file.write(lines_to_add)
        print(f"Added repo to {pacman_conf_path}")
    except Exception as e:
        print(f"Failed to add repo to {pacman_conf_path}: {str(e)}")


    # Add key
    System().command(recv_key_cmd, "Receiving key")
    System().command(lsign_key_cmd, "Signing key")
    System().command(update_pkg_cmd, "Updating package")



def mirrorlist():
    # Backup mirrorlist
    System().copy_file("/etc/pacman.d/mirrorlist", "/etc/pacman.d/mirrorlist.bak")

    # Install reflector
    PackageManagement().install("reflector")
    # Update mirrorlist
    System().command("sudo reflector --verbose --score 20 --fastest 5 --sort rate --save /etc/pacman.d/mirrorlist", "Updating mirrorlist")