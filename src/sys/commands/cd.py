from ..command import KernelCommand


class ChangeDirectoryCommand(KernelCommand):
    def __init__(self, kernel):
        super().__init__(kernel)

    def execute(self, args: [str]):
        path = args[0].split("/")
        # Remove All empty strings in List
        for i in range(len(path)):
            if path[i] == "":
                path.pop(i)

        # Split All Path Folders in Current Working Directory
        cwd_folders = self.kernel.working_dir.split("/")

        for folder in path:
            # Handle Different Folder CD operations
            if folder == "..":
                cwd_folders.pop(-1)

            elif folder == ".":
                pass

            else:
                # Update The Working Directory
                self.kernel.working_dir = ""
                for f in cwd_folders:
                    self.kernel.working_dir += f + "/"
                self.kernel.working_dir = self.kernel.working_dir.removesuffix("/")

                # Get Folders in Directory
                folders = self.kernel.execute_command("ls")

                # Check if folder exists, else raise an error
                if folder in folders:
                    cwd_folders.append(folder)
                else:
                    raise ValueError(
                        "Folder Not Found: " + self.kernel.working_dir + "/" + folder
                    )

        # Update The Working Directory
        self.kernel.working_dir = ""
        for f in cwd_folders:
            self.kernel.working_dir += f + "/"
        self.kernel.working_dir = self.kernel.working_dir.removesuffix("/")


command = {"name": "cd", "args_req": 1, "command": ChangeDirectoryCommand}
