from src.PackageManagement import PackageManagement
from src.System import System

def main():
    pm = PackageManagement(system=System())
    
    # Install packages from the system package manager.
    pm.install("vim")

if __name__ == "__main__":
    main()
