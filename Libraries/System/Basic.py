import sys

# Display Python version information
print("Python version:", sys.version)

# Display the platform where Python is running
print("Platform:", sys.platform)

# Display the path used for module search
print("Module search path:")
for path in sys.path:
    print(path)

# Display the list of loaded modules
print("Loaded modules:")
for module in sys.modules:
    print(module)

# Display the default string encoding
print("Default string encoding:", sys.getdefaultencoding())

sys.exit(0)