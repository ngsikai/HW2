from shunting_yard import *
from objects import *


def print_issue(qn, ans, result):
    print " "
    print "PROBLEM => " + qn
    print "MY ANSWER"
    print result
    print "ACTUAL ANSWER"
    print ans
    print " "

term_dict = { "a": [1, 1], "b": [2,2], "c": [3,3], "d": [4,4], "e": [5,5]}

A = Word("a", 1)
B = Word("b", 2)
C = Word("c", 3)
D = Word("d", 4)
E = Word("e", 5)

not_A = Word("a", 1)
not_A.toggle_is_not()
not_A_or_B = Query(A, B, "OR")
not_A_or_B.toggle_is_not()
not_A_and_B = Query(A, B, "AND")
not_A_and_B.toggle_is_not()

one = Query(C, D, "OR")
two = Query(one, not_A, "AND")
three = Query(B, two, "AND")
final = Query(A, three, "AND")

test_dict = {}
test_dict["A"] = A
test_dict["NOT A"] = not_A
test_dict["A OR B"] = Query(A, B, "OR")
test_dict["A AND B"] = Query(A, B, "AND")
test_dict["NOT A OR B"] = Query(not_A, B, "OR")
test_dict["NOT A AND B"] = Query(not_A, B, "AND")
test_dict["NOT (A AND B)"] = not_A_or_B
test_dict["NOT (A AND B)"] = not_A_and_B
test_dict["E OR B AND (C OR D) AND NOT A"] = final

for qn, ans in test_dict.items():
    res = get_query_obj(qn, term_dict)

    if not cmp(ans, res):
        print_issue(qn, ans, res)
