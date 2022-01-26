# template files for generating project files

# bot.py
CORE = {
    "IMPORT": """
# import cyan

from cyan import Session, Ticket
from cyan.event import ChannelMessageReceivedEvent
from cyan.model import ChannelMessage
    """.strip(),

    "SESSION": """
session = Session(app_url, Ticket("{app_id}", "{token}"))
    """.strip(),

    "RUN": """
    session.run()
    """.strip()
}
