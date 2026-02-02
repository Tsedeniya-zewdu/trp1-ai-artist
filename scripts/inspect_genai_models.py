import inspect
from google.genai import models

print('genai.models attrs sample:')
print([x for x in dir(models) if not x.startswith('_')][:400])

# Print callables and types that may relate to video generation
callables = [x for x in dir(models) if callable(getattr(models, x)) and not x.startswith('_')]
print('\ncallables:', callables)

# Inspect AsyncModels class if present
if hasattr(models, 'AsyncModels'):
    print('\nAsyncModels class attrs:', [x for x in dir(models.AsyncModels) if not x.startswith('_')][:400])

# Any functions containing 'video' or 'generate'
print('\nNames with video/generate:')
print([x for x in dir(models) if 'video' in x.lower() or 'generate' in x.lower()])

# Inspect docstrings for likely functions
for name in ['generate', 'generate_text', 'generate_image', 'generate_videos', 'generate_video', 'generate_stream']:
    if hasattr(models, name):
        print(f"\n{name} doc:\n", inspect.getdoc(getattr(models, name))[:400])
    else:
        print(f"\n{name} not found")
