from typing import Callable, Dict, Any, Optional


class Plugin:
    """
    cyanbot 插件类。

    初始化参数:
        name: 插件名称
        desc: 插件介绍（可选）
    """
    name: str
    desc: Optional[str]
    exported: Dict[str, Any]

    def __init__(self, name: str, desc: Optional[str] = None):
        self.name = name
        self.desc = desc if desc else ""
        self.exported = {}

    def export(self, name: str) -> Callable[[Any], Any]:
        """
        导出值/函数到插件空间。

        参数:
            name: 值/函数名称

        用法:
            >>> plugin = Plugin(...)

            >>> plugin.export("key")("value")

            >>> @plugin.export("key2")
            ... def func(x, y):
            ...     print(x, y)
            ...
        """
        def _export(data: Any):
            """
            将值/函数导出到插件。
            
            参数:
                data: 值/函数
            """
            self.exported[name] = data
            return data
        return _export
