from os import listdir
from ..command import KernelCommand


class ListCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        return listdir(self.kernel.working_dir)

    def execute_io(self, args: [str]):
        folders = self.execute(args)
        msg = ""
        for f in folders:
            msg += '"' + f + '"' + "  "

        return msg


command = {"name": "la", "args_req": 0, "command": ListCommand}
