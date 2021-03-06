# Examples of Word object:
# 1) bill
# 2) gates
# 3) computer
# 4) rich
# 
# Examples of Query object:
# 1) "bill AND gates" becomes
# => (bill,gates,AND)
# => This Query obj has:
# => Operand 1: bill - a Word obj
# => Operand 2: gates - a Word obj
# => Operator: AND
#
# 2) "bill AND gates OR computer" becomes
# => (computer,(bill,gates,AND),OR)
# => This Query obj has:
# => Operand 1: computer - a Word obj
# => Operand 2: (bill,gates,AND) - a Query obj
# => Operator: OR
#
# 3) "bill AND gates OR computer AND rich" becomes
# => ((bill,gates,AND),(computer,rich,AND),OR)
# => Operand 1: (bill,gates,AND) - a Query obj
# => Operand 2: (computer,rich,AND) - a Query obj
# => Operator: OR


class Word:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.is_not = False

    def get_value(self):
        return self.value

    def get_freq(self):
        return self.freq

    def set_freq(self, new_freq):
        self.freq = new_freq

    def get_is_not(self):
        return self.is_not

    def toggle_is_not(self):
        self.is_not = not(self.is_not)

    def __repr__(self):
        if self.is_not:
            return self.value + "!"
        else:
            return self.value

    def __str__(self):
        if self.is_not:
            return self.value + "!"
        else:
            return self.value

    def __eq__(self, other):
        if not isinstance(other, Word):
            return False
        else:
            return cmp(self.__dict__, other.__dict__)


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

    def set_freq(self, new_freq):
        self.freq = new_freq

    def get_is_not(self):
        return self.is_not

    def toggle_is_not(self):
        self.is_not = not(self.is_not)

    def __repr__(self):
        if self.is_not:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ",!)"
        else:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ")"

    def __str__(self):
        if self.is_not:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ",!)"
        else:
            return "(" + str(self.value1) + "," + str(self.value2) + "," + str(self.op) + ")"

    def __eq__(self, other):
        if not isinstance(other, Query):
            return False
        else:
            for v1, v2 in zip(self.__dict__, other.__dict__):
                if not cmp(v1, v2):
                    return False
            return True
