import os
import requests
import subprocess
from termcolor import colored

class PackageHandler:
    def __init__(self, packages):
        self.packages = packages

    def is_installed(self, package_name):
        return os.path.isfile(f"/pinecone/lib/{package_name}.py")

    
    def install(self, package_name):
        if self.is_installed(package_name):
            print(colored(f"Error: Library '{package_name}' is already installed", "red"))
            return

        package_url = self.get_package_url(package_name)
        if package_url:
            print(f"Installing '{package_name}' from {package_url}...")

        package_dep = self.get_package_dep(package_name)
        if package_dep:
            print(f"Installing dependencies: {package_dep}")
            install1 = f"pipx install {package_dep} || pip install {package_dep}"
            install2 = f"sudo apt-get -y update && sudo apt-get -y install python3-{package_dep}"
            process1 = subprocess.run(install1, shell=True, text=True, capture_output=True)
            process2 = subprocess.run(install2, shell=True, capture_output=True, text=True)


            response = requests.get(package_url)
            if response.status_code == 200:
                with open(f"/pinecone/lib/{package_name}.py", "wb") as f:
                    f.write(response.content)
                print(colored(f"Library '{package_name}' installed successfully!", "green"))
            else:
                print(colored(f"Error: Failed to download '{package_name}'", "red"))
        else:
            print(colored(f"Error: Package '{package_name}' not found", "red"))


    def uninstall(self, package_name):
        if not self.is_installed(package_name):
            print(colored(f"Error: Library '{package_name}' is not installed", "red"))
            return

        elif package_name != "package_handler" and package_name != "packages":
            os.remove(f"/pinecone/lib/{package_name}.py")
            print(colored(f"Library '{package_name}' uninstalled successfully!", "green"))

        else:
            print(colored("Error: Cannot remove package_handler and package list", 'red'))

    def list_installed(self):
        installed_packages = [f[:-3] for f in os.listdir("/pinecone/lib/") if f.endswith(".py")]
        if installed_packages:
            print("Installed packages:")
            for pkg in installed_packages:
                print(f" - {pkg}")
        else:
            print("No packages installed.")

    def get_package_url(self, package_name):
        for i in range(0, len(self.packages), 3):  
            if self.packages[i] == package_name:
                return self.packages[i + 1]
        return None

    def get_package_dep(self, package_name):
        for i in range(0, len(self.packages), 3):  
            if self.packages[i] == package_name:
                return self.packages[i + 2] if (i + 2) < len(self.packages) else None
        return None

    def run_package(self, package_name, command_parts):
        if self.is_installed(package_name) and command_parts is not None:
            subprocess.run(["python3", f"/pinecone/lib/{package_name}.py"] + command_parts[1:])
        elif self.is_installed(package_name) and command_parts is None:
            subprocess.run(["python3"], f"/pinecone/lib/{package_name}.py")
        else:
            print(colored(f"Error: Library '{package_name}' is not installed", "red"))
