import sys
import warnings
from concap import CommandTree

COMMANDS_HELP: str = """
命令:
    help                    显示帮助信息
    new/create/init         创建新项目实例
    run                     运行实例
    plugin                  管理插件
    exit                    退出程序
"""

HELP: str = f"""
cyanbot - 基于 Cyan SDK 的 QQ 机器人集成式管理工具

使用方法: cyanbot [命令] [参数]
{COMMANDS_HELP}
"""


# def cmd_n_fnd(tree, cmd, _):
#     tree.print(f"{cmd}: command not found. Enter 'help' for help.")


ctree: CommandTree = CommandTree()


@ctree.add_command("help")
def get_help(tree: CommandTree, cmd: str, arg: str) -> None:
    if arg:
        warnings.warn(f"调用指令 {cmd} 参数过多。")
        return
    tree.print(COMMANDS_HELP)


@ctree.add_command("init")
@ctree.add_command("create")
@ctree.add_command("new")
def new_instance(tree: CommandTree, _, arg: str) -> None:
    pass


@ctree.add_command("run")
def run_instance(tree: CommandTree, _, arg: str) -> None:
    pass


@ctree.add_command("plugin")
def manage_plugins(tree: CommandTree, _, arg: str) -> None:
    pass


@ctree.add_command("exit")
def exit_prog(tree: CommandTree, cmd: str, arg: str) -> None:
    if arg:
        warnings.warn(f"调用指令 {cmd} 参数过多。")
        return
    tree.run_command("logout", "")


if len(sys.argv) < 2:
    ctree.interactive()
else:
    ctree.run_command(sys.argv[1], "\t".join(sys.argv[2:]))
