

class Calculator():
    """
        This object uses common arithmetic operations to perform calculations.

        Usage:
        instantiate and call operators
    """

    def __init__(self):
        pass

    def add(self, **args:int) -> int:
        base = 0
        for key, value in args.items():
            base = base + value
        return base

