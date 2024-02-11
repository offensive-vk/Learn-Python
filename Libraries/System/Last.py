import sys

# Command-line arguments
print("Command-line arguments:", sys.argv)

# Python executable path
print("Python executable path:", sys.executable)

# Standard streams
print("Standard input stream:", sys.stdin)
print("Standard output stream:", sys.stdout)
print("Standard error stream:", sys.stderr)

# Memory management and garbage collection
print("Size of an empty list:", sys.getsizeof([]))
print("Reference count of an empty list:", sys.getrefcount([]))

# Interpreter interaction
print("Default encoding:", sys.getdefaultencoding())
print("Exception information:", sys.exc_info())

# System exit
try:
    sys.exit(1)
except SystemExit as e:
    print("SystemExit exception caught with exit status:", e)

# Maximum recursion depth
print("Maximum recursion depth limit before modification:", sys.getrecursionlimit())