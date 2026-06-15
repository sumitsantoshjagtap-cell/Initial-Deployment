"""NSE Portfolio Monitor — standalone launcher."""
from pathlib import Path
import pandas as pd
OUTPUT_DIR = Path("pipeline_outputs")
print("Artifacts at", OUTPUT_DIR.resolve())
