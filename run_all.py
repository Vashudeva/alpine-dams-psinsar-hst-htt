"""Run the full workflow in order.

Steps 02, 03 and the Figure 7 part of 05 need the temperature and reservoir-level
records in data/environment (see data/environment/README.md). Without them,
only the steps that use the PS data alone are run.
"""
import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from cancano_ps import config  # noqa: E402

env_ok = config.TEMPERATURE_CSV.exists() and config.RESERVOIR_CSV.exists()
steps = ["01_radial_projection.py", "02_crown_models.py", "03_crest_models.py",
         "04_anomaly_screening.py", "05_figures.py", "06_ps_summary.py"]
needs_env = {"02_crown_models.py", "03_crest_models.py"}

for s in steps:
    if s in needs_env and not env_ok:
        print(f"--- {s}: skipped (environmental records missing; see data/environment/README.md)")
        continue
    print(f"--- {s}")
    runpy.run_path(str(ROOT / "scripts" / s), run_name="__main__")
