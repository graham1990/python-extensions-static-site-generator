import sys
import importlib
from pathlib import Path


def load_module(directory, module_name):
    sys.path.insert(0, directory)
    importlib.import_module(module_name)
    sys.path.pop(0)
