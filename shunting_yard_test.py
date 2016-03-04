from shunting_yard import *
from objects import *


def print_issue(qn, ans, result):
    print " "
    print "PROBLEM => " + qn
    print "MY ANSWER"
    print result
    print "CORRECT ANSWER"
    print ans
    print " "

term_dict = {"a": [200, 0], "b": [1000, 0], "c": [10, 0], "d": [1, 0], "e": [20, 0], "f": [60, 0]}
term_dict["DOCUMENT_COUNT"] = 100000

test_dict = {}
test_dict["A"] = "a"
test_dict["NOT A"] = "a!"
test_dict["A OR B"] = "(a,b,OR)"
test_dict["A AND B"] = "(a,b,AND)"
test_dict["NOT A OR B"] = "(a!,b,OR)"
test_dict["NOT A AND B"] = "(a!,b,AND)"
test_dict["NOT (A OR B)"] = "(a,b,OR,!)"
test_dict["NOT (A AND B)"] = "(a,b,AND,!)"

test_dict["E OR B AND (C OR D) AND NOT A"] = "(e,(a!,(b,(c,d,OR),AND),AND),OR)"
test_dict["A AND B AND D"] = "(b,(a,d,AND),AND)"
test_dict["NOT A OR B OR NOT C"] = "(c!,(a!,b,OR),OR)"
test_dict["A AND B AND C OR D OR E"] = "(e,((b,(a,c,AND),AND),d,OR),OR)"
test_dict["(A AND C AND E) AND NOT (B AND D) AND F"] = "((b,d,AND,!),(f,(a,(e,c,AND),AND),AND),AND)"
# test_dict[""] = ""


for qn, ans in test_dict.items():
    res = get_query_obj(qn, term_dict)

    if ans != str(res):
        print_issue(qn, ans, res)