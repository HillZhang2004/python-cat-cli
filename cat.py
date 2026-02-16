'''
This program prints stdin to the screen.
'''
import sys
import shutil

def cat(file):
    src = getattr(file, "buffer", file)
    shutil.copyfileobj(src, sys.stdout.buffer)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin)
