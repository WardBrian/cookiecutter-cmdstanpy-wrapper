import shutil
import warnings
from pathlib import Path

import cmdstanpy

STAN_FILES_FOLDER = Path(__file__).parent / "stan"
CMDSTAN_VERSION = "{{ cookiecutter.cmdstan_version }}"


# on Windows specifically, we should point cmdstanpy to the repackaged
# CmdStan if it exists. This lets cmdstanpy handle the TBB path for us.
local_cmdstan = STAN_FILES_FOLDER / f"cmdstan-{CMDSTAN_VERSION}"
if local_cmdstan.exists():
    cmdstanpy.set_cmdstan_path(str(local_cmdstan.resolve()))
{% set models = cookiecutter.stan_files.split(',') %}
# Try to load the pre-compiled models. If that fails, compile them
try:
{% for item in models %}
    {{ item|trim|upper }} = cmdstanpy.CmdStanModel(
        exe_file=STAN_FILES_FOLDER / "{{ item|trim }}.exe",
        stan_file=STAN_FILES_FOLDER / "{{ item|trim }}.stan",
        compile=False,
    )
{% endfor %}
except ValueError:
    warnings.warn("Failed to load pre-built models, compiling")
{% for item in models %}
    {{ item|trim|upper }} = cmdstanpy.CmdStanModel(
        stan_file=STAN_FILES_FOLDER / "{{ item|trim }}.stan",
        stanc_options={"O1": True},
    )
    shutil.copy(
        {{ item|upper }}.exe_file,  # type: ignore
        STAN_FILES_FOLDER / "{{ item|trim }}.exe",
    )
{% endfor %}
# example: just print the info of the model
print({{ models[0]|trim|upper }}.exe_info())
