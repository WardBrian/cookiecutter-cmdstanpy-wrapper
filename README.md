# cookiecutter-cmdstanpy-wrapper

This project a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html)
template  designed for package developers who wish to wrap a [Stan](mc-stan.org)
model in a Python package.
It provides the ability to pre-compile the model as part
of a Python [wheel](https://pypi.org/project/wheel/), removing the need for end users
to have a C++ toolchain installed to install or use the package.

This uses [cmdstanpy](https://github.com/stan-dev/cmdstanpy) as the underlying interface to the Stan model.

If you're looking instead for a template for doing applied modeling work in CmdStanPy,
check out [cookiecutter-cmdstanpy-analysis](https://github.com/teddygroves/cookiecutter-cmdstanpy-analysis).


See an example based on the output of the template [here](https://github.com/WardBrian/stan_py_example)

## Usage

```
cookiecutter gh:WardBrian/cookiecutter-cmdstanpy-wrapper
```

This will ask you some basic prompts and then generate a folder with skeleton of a Python package.
This package will include the setup.py required for building the models as part of the wheel, and
a Github Actions script to do so on MacOS, Linux, and Windows using
[cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).

## How it works

The process of shipping a pre-compiled Stan model is a bit more complicated than it needs to be
due to Stan's reliance on Intel's [TBB](https://www.intel.com/content/www/us/en/developer/tools/oneapi/onetbb.html)
library.

To make a Stan model work in the most generality (e.g., on a machine it was not compiled on),
it needs to also have a compiled dynamic shared object for TBB. This is done by (optionally)
repackaging part of the CmdStan distribution alongside the built model. This allows TBB
to be detected on the new system. The built-in relocation tools in cibuildwheel ensure this
DSO is relocatable and that the compiled Stan models work.

The above behavior is only enabled when an environment variable called `PKG_NAME_REDISTRIBUTE_CMDSTAN` is set.
Source installations assume that the end user has a working CmdStan distribution already.


## License
This cookiecutter and the building code is licensed under the MIT license.

This project is modeled on work I assisted with on Facebook's
[prophet](https://github.com/facebook/prophet/) package, and the yet-unreleased
[scitkit-stan](https://github.com/WardBrian/scikit-stan) package.
