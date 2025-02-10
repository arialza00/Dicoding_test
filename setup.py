import sys
import subprocess

def install_requirements(file_path='requirements.txt'):
    try:
        with open(file_path, 'r') as file:
            requirements = file.readlines()
    except FileNotFoundError:
        print(f"File {file_path} not found. Please ensure the file exists in the specified location.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    for package in requirements:
        package = package.strip()
        if package:
            try:
                print(f"Installing {package}...")
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {package}. Error: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

    print("All packages installed successfully.")

if __name__ == "__main__":
    install_requirements()