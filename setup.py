import sys
import subprocess

def install_requirements(file_path='requirements.txt'):
    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
        for package in requirements:
            package = package.strip()
            if package:
                print(f"Installing {package}...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print("All packages installed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    install_requirements()