class Word:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.is_not = False

    def get_value(self):
        return self.value

    def get_freq(self):
        return self.freq

    def get_is_not(self):
        return self.is_not

    def toggle_is_not(self):
        self.is_not = not(self.is_not)

    def __repr__(self):
        if self.is_not:
            return self.value + "!"
        else:
            return self.value


class Query:
    def __init__(self, value1, value2, op):
        self.value1 = value1
        self.value2 = value2
        self.op = op
        if op == "AND":
            self.freq = min(value1.get_freq(), value2.get_freq())
        elif op == "OR":
            self.freq = value1.get_freq() + value2.get_freq()
        self.is_not = False

    def get_value1(self):
        return self.value1

    def get_value2(self):
        return self.value2

    def get_value2(self):
        return self.op

    def get_freq(self):
        return self.freq

    def get_is_not(self):
        return self.is_not

    def toggle_is_not(self):
        self.is_not = not(self.is_not)

    def __repr__(self):
        if self.is_not:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ",!)"
        else:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ")"
