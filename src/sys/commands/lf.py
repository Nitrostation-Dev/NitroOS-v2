from os.path import isfile
from os import listdir
from ..command import KernelCommand


class ListFilesCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        path = self.kernel.working_dir
        files = []

        for f in listdir(path):
            if isfile(path + "/" + f):
                files.append(f)

        return files

    def execute_io(self, args: [str]):
        folders = self.execute(args)
        msg = ""
        for f in folders:
            msg += '"' + f + '"' + "  "

        return msg


command = {"name": "lf", "args_req": 0, "command": ListFilesCommand}
