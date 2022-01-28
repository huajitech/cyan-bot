from cyan import Session
from cyanbot.plugin import Plugin
from typing import Optional


class Runtime:
    """
    机器人运行环境

    参数:
        session: 会话对象
    """
    def __init__(self, session: Session):
        self.session = session

    def register_plugin(self, plugin: Plugin):
        pass


runtime: Optional[Runtime] = None


def init_runtime(session: Session):
    global runtime
    runtime = Runtime(session)
