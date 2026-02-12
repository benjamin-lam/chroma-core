import sys
import importlib.util
import shutil

def check_module(name):
    return importlib.util.find_spec(name) is not None

def check_command(cmd):
    return shutil.which(cmd) is not None

print("\n=== Environment Check ===\n")

print("Python executable:", sys.executable)
print("Python version:", sys.version)

print("\nCommands:")
print("python3:", check_command("python3"))
print("pip3:", check_command("pip3"))

print("\nModules:")
print("venv:", check_module("venv"))
print("chromadb:", check_module("chromadb"))

print("\nDone.\n")