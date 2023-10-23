from ..command import KernelCommand

# from ..kernel import Kernel


class PwdCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        return self.kernel.working_dir

command = {
    "name": "pwd",
    "args_req": 0,
    "command": PwdCommand
}