from utils.log import LogMixin

class Calculator(LogMixin):
    """
        This object uses common arithmetic operations to perform calculations.

        Usage:
        instantiate and call operators
    """

    def add(self, **args:int) -> int:
        base = 0
        self.logger.info(f"the value for base is set to {base}")
        for key, value in args.items():
            base = base + value
        return base

