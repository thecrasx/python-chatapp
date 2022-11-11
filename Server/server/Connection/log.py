


class  Log:
    def __init__(self, type_, console=True):
        self.consoleEnabled = console
        self.type_ = type_

    def __call__(self, data):
        if self.consoleEnabled:
            print(f"[{self.type_}] {data}")

    