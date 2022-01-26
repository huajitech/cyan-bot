# template files for generating project files

# bot.py
CORE = {
    "IMPORT": """
# import cyan

from cyan import Session, Ticket
from cyanbot.runtime import init_runtime
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
init_runtime(session)
session.run()
    """.strip()
}

# pluginx.py
PLUGIN = {
    "IMPORT": """
# import cyan

from cyanbot.runtime import runtime

if runtime is None:
    raise Exception("Cyanbot is not running! You should start 'bot.py'.")

session = runtime.session
    """.strip(),
}
