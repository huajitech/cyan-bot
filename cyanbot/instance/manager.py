from concap import CommandTree

tree = CommandTree()


@tree.add_command("help")
def print_help(tree: CommandTree, _, arg: str) -> None:
    tree.print(
"""
命令:
    help                    输出此帮助信息
    new/create/init         创建新项目实例
"""
    )

def plugin(*args: str):
    tree.run_command(args[0], "")