from dotenv import load_dotenv
from pathlib import Path
import os
root = Path.cwd()
print('cwd', root)
for candidate in [root, root.parent, root.parent.parent]:
    env_path = candidate / '.env'
    print('check', candidate, env_path.exists())
    if env_path.exists():
        load_dotenv(env_path)
        print('loaded', env_path)
        break
print('OPENAI_API_KEY', os.environ.get('OPENAI_API_KEY'))
