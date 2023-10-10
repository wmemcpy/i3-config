from Class.PackageManagement import PackageManagement
from Class.System import System

def install_driver(Pm: PackageManagement):
    # Video drivers (AMD)
    Pm.install_lst([
        'mesa',
        'lib32-mesa',
        'vulkan-radeon',
        'lib32-vulkan-radeon',
        'vulkan-icd-loader',
        'lib32-vulkan-icd-loader',
        'vulkan-mesa-layers',
        'lib32-vulkan-mesa-layers'
    ])
