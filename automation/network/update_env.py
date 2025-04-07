import os
import subprocess


def check_for_updates():
    # Check for available updates using the package manager
    if os.name == 'posix':  # For Unix-like systems (e.g., Linux)
        subprocess.run(['apt', 'update'])  # Update package lists
        return subprocess.run(
            ['apt', 'list', '--upgradable'], capture_output=True, text=True
        ).stdout
    elif os.name == 'nt':  # For Windows systems
        return subprocess.run(
            ['wmic', 'qfe', 'list', 'full'], capture_output=True, text=True
        ).stdout
    else:
        return "Unsupported operating system"


def install_updates():
    # Install available updates using the package manager
    if os.name == 'posix':  # For Unix-like systems (e.g., Linux)
        subprocess.run(['apt', 'upgrade', '-y'])  # Upgrade packages
    elif os.name == 'nt':  # For Windows systems
        subprocess.run(['wuauclt', '/detectnow'])  # Force Windows
        # Update detection
    else:
        print("Unsupported operating system")


if __name__ == "__main__":
    print("Checking for available updates...")
    updates_available = check_for_updates()
    print(updates_available)
    if updates_available:
        print("Installing updates...")
        install_updates()
        print("Updates installed successfully.")
    else:
        print("No updates available.")
