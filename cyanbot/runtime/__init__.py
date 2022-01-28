from cyan import Session
from cyanbot.plugin import Plugin
from typing import Optional


class Context:
    """
    机器人运行环境

    参数:
        session: 会话对象
    """
    def __init__(self, session: Session):
        self.session = session

    def register_plugin(self, plugin: Plugin):
        pass


context: Optional[Context] = None


def init_context(session: Session):
    global context
    context = Context(session)
