import os
import sys


def before_all(context):
    os.makedirs("allure-results", exist_ok=True)
    with open("allure-results/environment.properties", "w") as f:
        f.write("os=macOS\n")
        f.write(f"python={sys.version.split()[0]}\n")
        f.write("env=local\n")
