from cyan import Session
from cyanbot.plugin import Plugin
from typing import Optional, Dict, Any, Set


class Context:
    """
    机器人运行环境

    参数:
        session: 会话对象
        env: 环境变量
    """
    session: Session
    env: Dict[str, Any]
    plugins: Set[Plugin]

    def __init__(self, session: Session, env: Optional[Dict[str, Any]] = None):
        self.session = session
        self.env = env if env else {}
        self.plugins = set()

    def register_plugin(self, plugin: Plugin) -> None:
        for pl in self.plugins:
            if plugin.name == pl.name:
                raise NameError(f"There's already a plugin named '{pl.name}'")
        self.plugins.add(plugin)

    def find_plugin_by_name(self, name: str) -> Optional[Plugin]:
        for pl in self.plugins:
            if pl.name == name:
                return pl


context: Optional[Context] = None


def init_context(session: Session):
    global context
    context = Context(session)
