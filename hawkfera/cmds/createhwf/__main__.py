import typing, sys
from .helper import help_function

def main(
    args: typing.List[str]
) -> int:
    print("Hello from createhwf!")
    help_function()
    return 0

exit(main(sys.argv))