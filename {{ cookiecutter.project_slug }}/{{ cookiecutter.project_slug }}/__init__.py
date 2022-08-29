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

def load_stan_model(name: str) -> cmdstanpy.CmdStanModel:
    """
    Try to load precompiled Stan models. If that fails,
    compile them.
    """
    try:
        model = cmdstanpy.CmdStanModel(
            exe_file=STAN_FILES_FOLDER / f"{name}.exe",
            stan_file=STAN_FILES_FOLDER / f"{name}.stan",
            compile=False,
        )
    except ValueError:
        warnings.warn(f"Failed to load pre-built model '{name}.exe', compiling")
        model = cmdstanpy.CmdStanModel(
            stan_file=STAN_FILES_FOLDER / f"{name}.stan",
            stanc_options={"O1": True},
        )
        shutil.copy(
            model.exe_file,  # type: ignore
            STAN_FILES_FOLDER / f"{name}.exe",
        )

    return model

{% set models = cookiecutter.stan_files.split(',') %}
{% for item in models %}
{{ item|trim|upper }} = load_stan_model("{{ item|trim }}")
{% endfor %}

# example: just print the info of the model
print({{ models[0]|trim|upper }}.exe_info())
