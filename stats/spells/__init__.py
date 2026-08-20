
from pathlib import Path
from importlib import import_module

__all__ = []

for file in Path(__file__).parent.glob('*.py'):  # take all files py from the current folder.
    if file.name.startswith('__'):  # skip __init__ file (and other private file).
        continue

    module = import_module(f'.{file.stem}', __name__)  # import current file.

    file_name_camel = ''.join([ w.capitalize() for w in file.stem.split('_') ])  # cast name file into camel case (to match class).
    
    class_of_file = vars(module).get(file_name_camel)  # get class from import file.

    if class_of_file == None:  # not found.
        continue

    globals()[file_name_camel] = class_of_file
    __all__.append(file_name_camel)  # use for allow import aster.