import subprocess
import sys
import warnings
from os import path, curdir, listdir
from concap import CommandTree
from cyanbot import instance
from cyanbot.instance import manager

COMMANDS_HELP: str = """
cyanbot - 基于 Cyan SDK 的 QQ 机器人集成式管理工具

命令:
    help                    显示帮助信息
    new/create/init         创建新项目实例
    run                     运行实例
    plugin                  管理插件
    exit                    退出程序
"""

HELP: str = f"""
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
    tree.print("正在生成实例......")
    instance.gen_base_file()
    tree.print("完成！")


@ctree.add_command("run")
def run_instance(tree: CommandTree, _, arg: str) -> None:
    if path.exists("bot.py"):
        botdir = curdir
    else:
        botdir = input("请输入 bot 实例路径：")
        if path.isfile(botdir):
            botdir, name = path.split(botdir)
            if name != "bot.py":
                raise ValueError("无效路径")
        else:
            if "bot.py" not in listdir(botdir):
                raise ValueError("无效路径")
    subprocess.run(["python", path.join(botdir, "bot.py")])


@ctree.add_command("plugin")
def manage_plugins(tree: CommandTree, _, arg: str) -> None:
    args = [a for a in arg.split(" ") if a]
    manager.plugin(*args)


@ctree.add_command("exit")
def exit_prog(tree: CommandTree, cmd: str, arg: str) -> None:
    if arg:
        warnings.warn(f"调用指令 {cmd} 参数过多。")
        return
    tree.run_command("logout", "")


def main():
    if len(sys.argv) < 2:
        ctree.run_command("help", "")
        ctree.interactive()
    else:
        ctree.run_command(sys.argv[1], "  ".join(sys.argv[2:]))

if __name__ == "__main__":
    main()