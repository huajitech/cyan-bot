from typing import Dict, Any, Optional


class Plugin:
    """
    cyanbot 插件类

    初始化参数:
        name: 插件名称
    """
    name: str
    desc: Optional[str]
    export: Dict[str, Any]

    def __init__(self, name: str, desc: Optional[str] = None):
        self.name = name
        self.desc = desc if desc else ""
        self.export = {}
