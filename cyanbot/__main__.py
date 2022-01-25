from concap import CommandTree

COMMANDS_HELP = """
Commands:
    help                    show help message
    new/create/init         create a new project
    run                     run an instance
    plugin                  manage plugins
"""

HELP = f"""
cyanbot - An integrated manager for Cyan Python SDK for QQ Bot

usage: cyanbot [command] [arguments]
{COMMANDS_HELP}
"""


# def cmd_n_fnd(tree, cmd, _):
#     tree.print(f"{cmd}: command not found. Enter 'help' for help.")


ctree = CommandTree()


@ctree.add_command("help")
def get_help(tree, _, arg):
    tree.print(COMMANDS_HELP)


@ctree.add_command("init")
@ctree.add_command("create")
@ctree.add_command("new")
def new_instance(tree, _, arg):
    pass


@ctree.add_command("run")
def run_instance(tree, _, arg):
    pass


@ctree.add_command("plugin")
def manage_plugins(tree, _, arg):
    pass


ctree.interactive()
