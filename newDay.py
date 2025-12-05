#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python new_day.py <day_number>")
        sys.exit(1)

    day = sys.argv[1]
    target = Path(f"Day{day}")
    template = Path("template")

    if target.exists():
        print(f"Error: {target} already exists.")
        sys.exit(1)

    shutil.copytree(template, target)
    print(f"Created {target} from template.")

if __name__ == "__main__":
    main()
