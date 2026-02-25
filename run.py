import sys
import os

# Add the current directory to sys.path to ensure src can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import posApp

if __name__ == '__main__':
    posApp().run()
