#!/usr/bin/env python
import pathlib

PROJECT_DIRECTORY = pathlib.Path(".")

{% set models = cookiecutter.stan_files.split(',') %}


if __name__ == '__main__':
    # create a stan file for each model desired
    for model in [{% for item in models %} "{{ item|trim }}", {% endfor %}]:
        (PROJECT_DIRECTORY /"{{ cookiecutter.project_slug }}"/ "stan" / (model + ".stan")).touch()

    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        (PROJECT_DIRECTORY / 'LICENSE').unlink()
