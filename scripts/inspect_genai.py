from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

try:
    from google import genai
    import os
    print("genai module loaded")
    api_key = os.environ.get("GEMINI_API_KEY", "")
    print("GEMINI_API_KEY set?", bool(api_key))
    client = genai.Client(api_key=api_key)
    print("client type:", type(client))
    aio = getattr(client, "aio", None)
    print("has aio:", bool(aio))
    if aio:
        print("aio attrs:", [x for x in dir(aio) if not x.startswith('_')])
        models = getattr(aio, "models", None)
        print("has models:", bool(models))
        if models:
            print("models attrs:", [x for x in dir(models) if not x.startswith('_')])
            callables = [m for m in dir(models) if callable(getattr(models, m)) and not m.startswith('_')]
            print("models callables:", callables)
        ops = getattr(aio, "operations", None)
        print("has operations:", bool(ops))
        if ops:
            print("operations attrs:", [x for x in dir(ops) if not x.startswith('_')])
    types = getattr(genai, "types", None)
    print("has types:", bool(types))
    if types:
        print("types attrs sample:", [x for x in dir(types) if not x.startswith('_')][:200])
except Exception as e:
    import traceback
    traceback.print_exc()
