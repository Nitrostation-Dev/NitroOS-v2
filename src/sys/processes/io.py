import os
from ..process import KernelProcess


class KernelIO(KernelProcess):
    def __init__(self, kernel):
        super().__init__(kernel, "kernel_io", os.getcwd())

    def execute_command(self, command: str) -> str:
        command_name, command_args = self.kernel.split_command(command)
        for cmd in self.kernel.commands:
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

    def execute_command_io(self, command_name: str, args: [str]) -> str:
        for command in self.kernel.commands:
            if command["name"] == command_name:
                if len(args) >= command["args_req"]:
                    cmd = command["command"](self)
                    return cmd.execute_io(args)

                else:
                    return "Args Not given"  # TODO: Type a better message

        else:
            return "No command found: " + command_name

    def update(self):
        input_command = input(self.working_dir + " $ ")
        cmd, args = self.kernel.split_command(input_command)
        print(self.execute_command_io(cmd, args), "\n")
