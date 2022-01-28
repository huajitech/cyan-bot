from . import template
from typing import Optional
from os import path, curdir, makedirs


def gen_base_file(basedir: Optional[str] = None):
    if basedir is None:
        basedir = curdir

    plugs_dir = path.join(basedir, "plugins")
    makedirs(plugs_dir)
    with open(path.join(plugs_dir, "__init__.py"), "w") as f:
        f.write(template.PLUGIN["INIT"])


def gen_bot_py(
    app_url: str, app_id: str, token: str,
    basedir: Optional[str] = None
):
    if basedir is None:
        basedir = curdir

    with open(path.join(basedir, "bot.py"), "w") as f:
        f.write(template.CORE["IMPORT"])
        f.write("\n\n")
        f.write(template.CORE["CONFIG"].format(
            (app_url, app_id, token)
        ))
        f.write("\n\n")
        f.write(template.CORE["SESSION"])
        f.write("\n\n")
        f.write(template.CORE["RUN"])


def gen_plugin(
    *,
    basedir: Optional[str] = None,
    name: Optional[str] = None
):
    if name is None:
        name = "插件名称"
    if basedir is None:
        basedir = path.join(curdir, "plugins", name)

    with open(path.join(basedir, "__init__.py"), "w") as f:
        f.write(template.PLUGIN["IMPORT"].format(name))
