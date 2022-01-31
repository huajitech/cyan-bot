from typing import Optional
from os import path, curdir, chdir
from cookiecutter.main import cookiecutter  # type: ignore


def gen_base_file(basedir: Optional[str] = None):
    """
    生成实例基本文件。

    参数:
        basedir: 生成实例的根路径
    """
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
    """
    生成插件基本文件。

    参数:
        basedir: 生成插件的根路径
    """
    workdir = None
    if basedir:
        workdir = path.abspath(curdir)
        chdir(basedir)
    cookiecutter(
        "https://gitlab.huajitech.net/huajitech/cookiecutter-cyanbot-plugin"
    )
    if workdir:
        chdir(workdir)
