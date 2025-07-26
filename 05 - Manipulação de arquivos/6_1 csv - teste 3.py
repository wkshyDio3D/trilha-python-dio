
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    pass
except IOError as exc:
    print(f'erro ao criar o arquivo. {exc}')