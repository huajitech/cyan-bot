from typing import Callable, Dict, Any, Optional


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

    def set_data(self, name: str) -> Callable[[Any], Any]:
        def _set_data(data: Any):
            self.export[name] = data
            return data
        return _set_data
