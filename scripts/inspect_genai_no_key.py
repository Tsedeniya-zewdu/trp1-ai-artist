import inspect
from google import genai

print("genai attrs (sample):")
print([x for x in dir(genai) if not x.startswith('_')][:200])

# types
types = getattr(genai, 'types', None)
print('\nhas types:', bool(types))
if types:
    print('types sample:', [x for x in dir(types) if 'Video' in x or 'Generate' in x or 'video' in x or 'Generate' in x][:200])

# client class
Client = getattr(genai, 'Client', None)
print('\nHas Client:', bool(Client))
if Client:
    print('Client attributes sample:', [x for x in dir(Client) if not x.startswith('_')][:200])

# look for functions referencing 'video' in module
print('\nSearching module for video-related names:')
names = []
for name in dir(genai):
    if 'video' in name.lower() or 'generate' in name.lower():
        names.append(name)
print(names)

# check genai.aio if available without initializing client
aio = getattr(genai, 'aio', None)
print('\naio available at module-level?:', bool(aio))
if aio:
    print('aio attrs:', [x for x in dir(aio) if not x.startswith('_')])

# check submodules
try:
    import google.genai
    import pkgutil
    pkg = google.genai
    print('\nSubmodules:')
    for importer, modname, ispkg in pkgutil.iter_modules(pkg.__path__):
        print(modname, 'pkg' if ispkg else 'module')
except Exception as e:
    print('Could not list submodules:', e)
