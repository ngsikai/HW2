from objects import *
from nltk.stem.porter import *


def get_query_obj(query_str, dictionary):
    return querify(get_postfix(query_str, dictionary))


def get_postfix(infix, dictionary):
    tokens_list = add_whitespaces(infix).split()
    postfix = []
    op_stack = []
    stemmer = PorterStemmer()

    while tokens_list:
        current_token = tokens_list.pop(0)

        if is_variable(current_token):
            current_token = stemmer.stem(current_token).lower()
            term_freq = 0
            if current_token in dictionary:
                term_freq = dictionary[current_token][0]
            word_obj = Word(current_token, term_freq)
            postfix.append(word_obj)

        elif is_operator(current_token):
            while op_stack:
                if is_operator(op_stack[-1]) and is_precedent(op_stack[-1], current_token):
                    postfix.append(op_stack.pop())
                else:
                    break
            op_stack.append(current_token)

        elif current_token == "(":
            op_stack.append(current_token)

        elif (current_token == ")"):
            while(op_stack and op_stack[-1] != "("):
                postfix.append(op_stack.pop())
            op_stack.pop()  # remove "(" from op_stack

    while op_stack:
        postfix.append(op_stack.pop())

    return postfix


def querify(postfix):
    index = 1
    while len(postfix) > 1:
        element = postfix[index]
        if element == "AND" or element == "OR":
            operand1 = postfix[index - 2]
            operand2 = postfix[index - 1]
            query_obj = Query(operand1, operand2, element)
            postfix[index - 2] = query_obj
            postfix.pop(index - 1)
            postfix.pop(index - 1)
            index -= 2
        elif element == "NOT":
            operand = postfix[index - 1]
            operand.toggle_is_not()
            postfix.pop(index)
            # index remains the same
        else:
            index += 1
    return postfix[0]


def optimize_postfix(postfix, index):
    chain_count = 1
    operation = postfix[index]
    while index < len(postfix) - 1:
        if postfix[index + 1] == operation:
            chain_count += 1
            index += 1
        else:
            # go back to the last element of the chain
            index -= 1
            break
    if chain_count is not 1:
        right_bound = index - chain_count
        left_bound = right_bound - chain_count
        term_list = postfix[left_bound:right_bound + 1]
        for i in range(left_bound, right_bound + 1):
            highest_freq_term = max(term_list, key=lambda x: x.get_freq())
            postfix[i] = highest_freq_term
            term_list.remove(highest_freq_term)
    return postfix


def add_whitespaces(str):
    processed_str = ""
    for char in str:
        if char == "(":
            processed_str += char + " "
        elif char == ")":
            processed_str += " " + char
        else:
            processed_str += char
    return processed_str


def is_precedent(stack_token, current_token):
    global precedence_dict
    return precedence_dict[stack_token] < precedence_dict[current_token]


def is_operator(token):
    if token == "OR" or token == "AND" or token == "NOT":
        return True
    else:
        return False


def is_variable(token):
    if token == "OR" or token == "AND" or token == "NOT":
        return False
    elif token == "(" or token == ")":
        return False
    else:
        return True

precedence_dict = {"OR": 3, "AND": 2, "NOT": 1}

# TEST
# A_obj = Word("A", 0, False)
# B_obj = Word("B", 0, False)
# test_list = []
# test_list.append(A_obj)
# test_list.append(B_obj)
# test_list.append("OR")
# print test_list

#test_dict = {"A": [200, 0], "B": [1000, 0], "C": [1000, 0], "D": [1, 0]}

# infix = "A AND (B AND C) AND D"
# print get_postfix(infix, test_dict)
# print get_query_obj(infix, test_dict)
