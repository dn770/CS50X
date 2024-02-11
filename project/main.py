from initial_boot import initial_boot
from ongoing_loop import ongoing_loop


def main():
    management_system = initial_boot()
    ongoing_loop(management_system)
    return


main()
