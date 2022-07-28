# cookiecutter-cmdstan-wrapper

This project a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html)
template  designed for package developers who wish to wrap a [Stan](mc-stan.org)
model in a Python package.
It provides the ability to pre-compile the model as part
of a Python [wheel](https://pypi.org/project/wheel/), removing the need for end users
to have a C++ toolchain installed to install or use the package.

This uses [cmdstanpy](https://github.com/stan-dev/cmdstanpy) as the underlying interface to the Stan model.

If you're looking instead for a template for doing applied modeling work in CmdStanPy,
check out [cookiecutter-cmdstanpy-analysis](https://github.com/teddygroves/cookiecutter-cmdstanpy-analysis).

## Usage

```
cookiecutter gh:WardBrian/cookiecutter-cmdstan-wrapper
```

This will ask you some basic prompts and then generate a folder with skeleton of a Python package.
This package will include the setup.py required for building the models as part of the wheel, and
a Github Actions script to do so on MacOS, Linux, and Windows using
[cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).


## License
This cookiecutter and the building code is licensed under the MIT license.

This project is modeled on work I assisted with on Facebook's
[prophet](https://github.com/facebook/prophet/) package, and the yet-unreleased
[scitkit-stan](https://github.com/WardBrian/scikit-stan) package.
