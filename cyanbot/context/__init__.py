from cyan import Session
from cyanbot.plugin import Plugin
from typing import Optional, Dict, Any


class Context:
    """
    机器人运行环境。

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
        """
        按名称查找插件。

        参数:
            name: 插件名称

        返回值:
            若存在该名称的插件，则返回对应的插件对象，否则返回 None。
        """
        return self.plugins.get(name, None)

    def register_plugin(self, plugin: Plugin) -> None:
        """
        注册插件到上下文。

        参数:
            plugin: 插件对象
        """
        if self.find_plugin_by_name(plugin.name):
            raise ValueError(f"There's already a plugin named '{plugin.name}'")
        self.plugins[plugin.name] = plugin


context: Optional[Context] = None


def init_context(session: Session):
    """
    初始化上下文。

    参数:
        session: 会话对象
    """
    global context
    context = Context(session)
