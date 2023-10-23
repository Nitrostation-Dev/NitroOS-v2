class KernelProcess:
    def __init__(self, kernel, name, working_dir):
        self.kernel = kernel
        self.id = 0
        self.name = name
        self.working_dir = working_dir

    def update(self):
        pass

    def shutdown(self):
        pass