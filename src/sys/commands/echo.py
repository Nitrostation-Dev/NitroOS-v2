from ..command import KernelCommand


class EchoCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        msg = ""
        for arg in args:
            msg += arg + " "

        return msg


command = {"name": "echo", "args_req": 1, "command": EchoCommand}
