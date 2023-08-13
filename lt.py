from argparse import ArgumentParser
from pathlib import Path
from typing import Type
from json import load
from subprocess import run
from filecmp import cmp
from queue import Queue


# ASCII basic colors
class Color:
    reset = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"

# Colorful print
def cprint(message: str, color: Type[Color]) -> None:
    print(f"{color}{message}{Color.reset}")

def ok(message: str) -> None:
    cprint(message, Color.green)

def err(message: str) -> None:
    cprint(message, Color.red)

# JSON scheme valid options
class SchemeJSON:
    platform_options = ["Unix", "Windows"]

    def is_valid(key: str, key_options: list) -> bool:
        return key in key_options


def main():
    # Setup
    parser = ArgumentParser()
    parser.add_argument("-p", "--program", help="program pathname", type=str, required=True)
    parser.add_argument("-c", "--compile", help="compile program (default=False)", action="store_true")
    args = parser.parse_args()

    NAME = "lt.py"

    lt_workspace = Path(__file__).parent
    program: str = args.program # program name with path
    should_compile: bool = args.compile 

    # Remove file extention if provided
    if Path(program).stem != program:
        program = str(Path(program).with_suffix(""))

    # JSON settings
    with open(lt_workspace / "config.json", "r") as config_file:
        config_data = load(config_file)

        compiler: str = config_data["compiler"]
        platform: str = config_data["platform"]

    # Choose correct way of running executable
    if platform == "Windows":
        executable: str = program + ".exe"
    elif platform == "Unix":
        executable: str = program

    # Exit before errors can occur
    if not SchemeJSON.is_valid(platform, SchemeJSON.platform_options):
        print(f"{NAME}: error: invalid platform {platform} (config.json)")
        exit()
    if not Path.is_dir(Path(program + "-tests")):
        print(f"{NAME}: error: no {program}-tests directory")
        exit()

    # Compile
    if should_compile:
        run([compiler, program + ".cpp", "-o", program], shell=True)

    # Compare program output with expected results
    output_queue = Queue()
    counter = 0
    mx = 0

    for x in Path(program + "-tests").iterdir():
        if x.suffix == ".in":
            run([executable], stdin=x.open("r"), stdout=(lt_workspace / "lt.txt").open("w"))

            if cmp(str(x.with_suffix(".out")), lt_workspace / "lt.txt"):
                ok(str(x.stem) + ": OK")
                counter += 1
            else:
                err(str(x.stem) + ": WA")
                output_str = str(x.stem) + "\n"
                with open(x.with_suffix(".out"), "r") as f:
                    output_str += "expected:\n" + f.read() + "\n"
                with open(lt_workspace / "lt.txt", "r") as f:
                    output_str += "program output:\n" + f.read()
                output_queue.put(output_str)
            # open(lt_workspace / "lt.txt", "w").close() # clear temporary file
            mx += 1
    
    # Print wrong program output
    print("\nwrong outputs")
    print("-------------")
    while not output_queue.empty():
        y: list = output_queue.get()
        
        # y contains 3 strings
        # this is safe
        # trust me, bro
        cprint("*****", Color.magenta)
        print(y)
        cprint("*****", Color.magenta)
    print("-------------\n")

    # Print results
    if counter == mx:
        ok(str(counter) + "/" + str(mx))
    else:
        err(str(counter) + "/" + str(mx))


if __name__ == "__main__":
    main()
