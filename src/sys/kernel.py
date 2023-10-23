import os

from .commands.pwd import command as pwdCommand
from .commands.echo import command as echoCommand
from .commands.ls import command as lsCommand
from .commands.lf import command as lfCommand
from .commands.la import command as laCommand
from .commands.cd import command as cdCommand

from .process import KernelProcess
from .processes.io import KernelIO


class Kernel:
    # ============[Kernel Functions]============
    def __init__(self):
        # Kernel Variables
        self.running = True
        self.working_dir = os.getcwd() + "/src"

        self.commands = [pwdCommand, echoCommand, lsCommand, lfCommand, laCommand, cdCommand]
        self.processes = []

        self.add_process(KernelIO(self))

    def start_kernel(self):
        self.loop()

    def loop(self):
        while self.running:
            for process in self.processes:
                process.update()

        self.shutdown()

    def shutdown(self):
        for process in self.processes:
            process.shutdown()

    # ============[Command Functions]============
    def split_command(self, command: str):
        args = command.split(" ")
        return (args[0], args[1:])

    def execute_command(self, command: str) -> str:
        command_name, command_args = self.split_command(command)
        for cmd in self.commands:
            if cmd["name"] == command_name:
                if len(command_args) >= cmd["args_req"]:
                    _ = cmd["command"](self)
                    return _.execute(command_args)

                else:
                    raise ValueError(
                        "Not Enough Arguments Provided"
                    )  # TODO: Create custom errors

        else:
            raise ValueError("Command Not Found")  # TODO: Create custom errors

    # ============[Process Functions]============
    def add_process(self, process: KernelProcess):
        process.id = len(self.processes)
        self.processes.append(process)
