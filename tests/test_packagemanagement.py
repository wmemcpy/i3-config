import unittest
from unittest.mock import Mock
from src.PackageManagement import PackageManagement

class TestPackageManagement(unittest.TestCase):

    def setUp(self):
        self.mock_system = Mock()
        self.package_management = PackageManagement(system_package="pacman", aur="yay", system=self.mock_system)
        
    def test_system_install(self):
        package_name = "example-package"
        self.package_management._PackageManagement__system_install(package_name)
        self.mock_system.command.assert_called_once_with(f"sudo pacman -S --noconfirm --needed {package_name}", f"Installing {package_name}")

    def test_aur_install(self):
        package_name = "example-package"
        self.package_management._PackageManagement__aur_install(package_name)
        
        self.mock_system.command.assert_called_once_with(f"yay -S --noconfirm --needed {package_name}", f"Installing {package_name}")

    def test_update_mirror(self):
        self.package_management.update_mirror()
        
        self.mock_system.command.assert_called_once_with("sudo pacman -Syy", "Updating mirrorlist")

    def test_update_system(self):
        self.package_management.update_system()
        
        self.mock_system.command.assert_called_once_with("sudo pacman -Syu --noconfirm", "Updating system")

    def test_install(self):
        package_name = "example-package"
        
        self.package_management.install(package_name)
        self.mock_system.command.assert_called_once_with(f"sudo pacman -S --noconfirm --needed {package_name}", f"Installing {package_name}")
        
        self.package_management.install(package_name, aur=True)
        self.mock_system.command.assert_called_with(f"yay -S --noconfirm --needed {package_name}", f"Installing {package_name}")

    def test_install_lst(self):
        package_list = ["package1", "package2"]
        
        self.package_management.install_lst(package_list)
        
        self.assertEqual(self.mock_system.command.call_count, len(package_list))
        self.mock_system.command.assert_called_with(f"yay -S --noconfirm --needed {package_list[-1]}", f"Installing {package_list[-1]}")
