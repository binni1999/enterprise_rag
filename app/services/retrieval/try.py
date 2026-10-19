import sys
from pathlib import Path

# Add project root to sys.path so 'app' package is resolvable
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from app.config import settings
print("yo")