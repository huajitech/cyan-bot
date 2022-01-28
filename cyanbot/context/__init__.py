from cyan import Session
from cyanbot.plugin import Plugin
from typing import Optional, Dict, Any


class Context:
    """
    机器人运行环境

    参数:
        session: 会话对象
        env: 环境变量
    """
    session: Session
    env: Dict[str, Any]
    plugins: Dict[str, Plugin]

    def __init__(self, session: Session, env: Optional[Dict[str, Any]] = None):
        self.session = session
        self.env = env if env else {}
        self.plugins = {}

    def find_plugin_by_name(self, name: str) -> Optional[Plugin]:
        for pl in self.plugins:
            if self.plugins[pl].name == name:
                return pl

    def register_plugin(self, plugin: Plugin) -> None:
        if self.find_plugin_by_name(plugin.name):
            raise ValueError(f"There's already a plugin named '{plugin.name}'")
        self.plugins[plugin.name] = plugin


context: Optional[Context] = None


def init_context(session: Session):
    global context
    context = Context(session)
