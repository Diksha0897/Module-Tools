from enum import Enum


class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"


os1 = OperatingSystem.MACOS
os2 = OperatingSystem.UBUNTU

print(os1)
print(os1.value)

if os1 == OperatingSystem.MACOS:
    print("User prefers macOS")