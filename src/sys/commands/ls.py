from genericpath import isdir
from os import listdir
from ..command import KernelCommand


class ListFoldersCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        path = self.kernel.working_dir
        folders = []

        for f in listdir(path):
            if isdir(path + "/" + f):
                folders.append(f)

        return folders

    def execute_io(self, args: [str]):
        folders = self.execute(args)
        msg = ""
        for f in folders:
            msg += '"' + f + '"' + "  "

        return msg


command = {"name": "ls", "args_req": 0, "command": ListFoldersCommand}
