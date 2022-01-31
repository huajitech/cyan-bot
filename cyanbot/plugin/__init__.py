from typing import Callable, Dict, Any, Optional


class Plugin:
    """
    cyanbot 插件类

    初始化参数:
        name: 插件名称
    """
    name: str
    desc: Optional[str]
    exported: Dict[str, Any]

    def __init__(self, name: str, desc: Optional[str] = None):
        self.name = name
        self.desc = desc if desc else ""
        self.exported = {}

    def export(self, name: str) -> Callable[[Any], Any]:
        def _export(data: Any):
            self.exported[name] = data
            return data
        return _export
