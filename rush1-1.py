import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'rush-1-1'))
from rush import rush

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid size", file=sys.stderr)
        sys.exit(1)
    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        rush(x, y)
    except ValueError:
        print("Invalid size", file=sys.stderr)
        sys.exit(1)
