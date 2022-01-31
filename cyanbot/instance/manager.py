from concap import CommandTree
from os import path, curdir, listdir
from cyanbot import instance
import warnings

ctree = CommandTree()


@ctree.add_command("help")
def print_help(tree: CommandTree, _, arg: str) -> None:
    tree.print(
        """
命令:
    help                    输出此帮助信息
    new/create/init         创建新插件
    exit                    退出程序
"""
    )


@ctree.add_command("init")
@ctree.add_command("create")
@ctree.add_command("new")
def new_instance(tree: CommandTree, _, arg: str) -> None:
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
    tree.print("正在生成插件......")
    instance.gen_plugin(path.join(botdir, "plugins"))
    tree.print("完成！")


@ctree.add_command("exit")
def exit_prog(tree: CommandTree, _, arg: str) -> None:
    if arg:
        warnings.warn("调用指令 exit 参数过多。")
        return
    tree.run_command("logout", "")


def plugin(*args: str):
    if args:
        ctree.run_command(args[0], "")
    else:
        ctree.interactive("plugin> ")
