from shunting_yard import *

dict = {}
dict["A OR B"] = ["A", "B", "OR"]
dict["A AND B"] = ["A", "B", "AND"]
dict["NOT A"] = ["A", "NOT"]

dict["NOT A OR B"] = ["A", "NOT", "B", "OR"]
dict["NOT A AND B"] = ["A", "NOT", "B", "AND"]
dict["NOT (A OR B)"] = ["A", "B", "OR", "NOT"]
dict["NOT (A AND B)"] = ["A", "B", "AND", "NOT"]
dict["A OR B AND (C OR D) AND NOT E"] = ["A", "B", "C", "D", "OR", "E", "NOT", "AND", "AND", "OR"]

for qn, ans in dict.items():
    result = get_postfix(qn)
    if (len(result) != len(ans)):
        print_issue(qn, ans, result)
        break
    for a, b in zip(result, ans):
        if (str(a) != str(b)):
            print_issue(qn, ans, result)
            break


def print_issue(qn, ans, result):
    print " "
    print "PROBLEM => " + qn
    print "MY ANSWER"
    print result
    print "ACTUAL ANSWER"
    print ans
    print " "
