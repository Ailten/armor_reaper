
# import all class.
from pathlib import Path
from importlib import import_module


__all__ = []

# browse all files.
for file in Path(__file__).parent.glob('*.py'):

    # skip file init (and others).
    if file.name.startswith('__'):
        continue

    # import current file.
    module = import_module(f'.{file.stem}', __name__)
    
    # browse var (as dict).
    for k,v in vars(module).items():

        # skip var not router.
        if not type(v).__name__ == "APIRouter":
            continue

        # add it.
        globals()[k] = v
        __all__.append(k)