from src.sys.kernel import Kernel


def start_kernel():
    print("bootloader started")
    kernel = Kernel()
    kernel.start_kernel()
