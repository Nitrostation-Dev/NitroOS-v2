# from .kernel import Kernel


class KernelCommand:
    def __init__(self, kernel):
        self.kernel = kernel

    def execute(self, args: [str]):
        pass

    def execute_io(self, args: [str]):
        message = self.execute(args)
        return "" if message is None else message
