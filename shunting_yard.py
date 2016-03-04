from objects import *
from nltk.stem.porter import *


document_count = 0


# Function that takes in raw query as query_str and dictionary
# to output the Query object
def get_query_obj(query_str, dictionary):
    global document_count
    document_count = dictionary["DOCUMENT_COUNT"]
    return querify(get_postfix(query_str, dictionary))


# Helper function that takes in infix string and dictionary
# to output the postfix list
# using the shunting yard algorithm
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


# Helper function that takes in postfix list
# to output the Query object
def querify(postfix):
    global document_count
    index = 1
    while len(postfix) > 1:
        element = postfix[index]
        if element == "AND" or element == "OR":
            postfix = optimize_postfix(postfix, index)
            operand1 = postfix[index - 2]
            operand2 = postfix[index - 1]
            query_obj = Query(operand1, operand2, element)
            # replace operand1, operand2 and element with query_obj
            postfix[index - 2] = query_obj
            postfix.pop(index - 1)
            postfix.pop(index - 1)
            index -= 2
        elif element == "NOT":
            operand = postfix[index - 1]
            operand.toggle_is_not()
            operand.set_freq(document_count - operand.get_freq())
            postfix.pop(index)
            # index remains the same
        else:
            index += 1
    return postfix[0]


# Helper function that takes in postfix list and index of operator
# to output a reordered postfix list
# that is optimised based on term frequency of operands
def optimize_postfix(postfix, index):
    chain_count = 1
    operation = postfix[index]
    while index + 1 < len(postfix):
        index += 1
        if postfix[index] == operation:
            chain_count += 1
        else:
            # go back to the last element of the chain
            index -= 1
            break
    if chain_count is not 1:
        right_bound = index - chain_count
        left_bound = right_bound - chain_count
        term_list = postfix[left_bound:right_bound + 1]
        # loop: choose operand of highest frequency and update postfix list
        for i in range(left_bound, right_bound + 1):
            max_term = term_list[0]
            max_term_index = 0
            for index, element in enumerate(term_list):
                if element.get_freq() > max_term.get_freq():
                    max_term = element
                    max_term_index = index
            postfix[i] = max_term
            term_list.pop(max_term_index)
    return postfix


# Helper function that adds whitespaces after "(" and before ")"
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
