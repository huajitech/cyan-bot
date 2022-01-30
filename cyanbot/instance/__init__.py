from typing import Optional
from os import path, curdir, chdir
from cookiecutter.main import cookiecutter  # type: ignore


def gen_base_file(basedir: Optional[str] = None):
    workdir = None
    if basedir:
        workdir = path.abspath(curdir)
        chdir(basedir)
    cookiecutter(
        "https://gitlab.huajitech.net/huajitech/cookiecutter-cyanbot-instance"
    )
    if workdir:
        chdir(workdir)


def gen_plugin(basedir: Optional[str] = None):
    workdir = None
    if basedir:
        workdir = path.abspath(curdir)
        chdir(basedir)
    cookiecutter(
        "https://gitlab.huajitech.net/huajitech/cookiecutter-cyanbot-plugin"
    )
    if workdir:
        chdir(workdir)