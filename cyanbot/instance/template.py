# template files for generating project files

# bot.py
CORE = {
    "IMPORT": """
# import cyan

from cyan import Session, Ticket
from cyanbot.context import init_context
    """.strip(),

    "CONFIG": """
app_url = "{0}"
app_id = "{1}"
token = "{2}"
    """.strip(),

    "SESSION": """
session = Session(app_url, Ticket(app_id, token))
    """.strip(),

    "RUN": """
init_context(session)

__import__(".plugins")

session.run()
    """.strip()
}

# pluginx.py
PLUGIN = {
    "IMPORT": """
# import cyan

from cyanbot.context import context

if context is None:
    raise Exception("Cyanbot is not running! You should start 'bot.py'.")

session = context.session
    """.strip(),

    "INIT": """
# 该文件用于控制该目录下插件的导入。
# 你可以以 import 的形式自行控制想导入的插件。
# 若想导入该目录下的所有插件，可以取消注释下面一行：
# from . import *
    """.strip()
}
