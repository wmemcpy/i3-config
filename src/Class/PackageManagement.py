from src.Class.System import System


class PackageManagement(System):
    def __init__(self, system_package: str = "pacman", aur: str = "yay", log_file: str = "log.log", log: bool = True) -> None:
        super().__init__(log_file=log_file, log=log)

        self.system_package = system_package
        self.aur = aur

    # def __system_install(self, package: str) -> None:
    #     self.command(
    #         f"sudo {self.system_package} -S --noconfirm --needed {package}", f"Installing {package}")

    def __aur_install(self, package: str) -> None:
        self.command(
            f"{self.aur} -S --noconfirm --needed {package}", f"Installing {package}")

    def __faltapk_install(self, package: str) -> None:
        self.command(f"flatpak install -y {package}", f"Installing {package}")

    def update_mirror(self) -> None:
        self.command(f"sudo {self.system_package} -Syyuu",
                     "Updeating mirrorlist")

    def update_system(self) -> None:
        self.command(
            f"sudo {self.system_package} -Syu --noconfirm", "Updating system")

    def install(self, package: str, flatpak: bool = False) -> None:
        self.__aur_install(
            package) if not flatpak else self.__faltapk_install(package)

    def install_lst(self, packages: list[str], flatpak: bool = False) -> None:
        for package in packages:
            self.install(package, flatpak)
