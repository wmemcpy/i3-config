from src.System import System


class PackageManagement:
    def __init__(self, system_package: str = "pacman", aur: str = "yay", system: System = None) -> None:
        self.system_package = system_package
        self.aur = aur
        self.system = system

    def __system_install(self, package: str) -> None:
        self.system.command(f"sudo {self.system_package} -S {package}", f"Installing {package}")

    def __aur_install(self, package: str) -> None:
        self.system.command(f"{self.aur} -S {package}", f"Installing {package}")

    def install(self, package: str, aur: bool = False) -> None:
        self.__aur_install(package) if aur else self.__system_install(package)

    def install_lst(self, packages: list[str], aur: bool = True) -> None:
        for package in packages:
            self.install(package, aur)
