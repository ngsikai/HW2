import math


def merge(list1, list2, op):
    if (op == "AND"):
        return merge_and(list1, list2)
    elif (op == "OR"):
        return merge_or(list1, list2)


def merge_and(list1, list2):
    result = []
    ptr1 = 0
    ptr2 = 0
    list1_len = len(list1)
    list1_skip = int(math.floor(math.sqrt(list1_len)))
    list2_len = len(list2)
    list2_skip = int(math.floor(math.sqrt(list2_len)))
    while ptr1 < list1_len and ptr2 < list2_len:
        if list1[ptr1] == list2[ptr2]:
            result.append(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif list1[ptr1] < list2[ptr2]:
            # check for skip_pointer in list1
            projected_skip = ptr1 + list1_skip
            if ptr1 % list1_skip == 0 and projected_skip < list1_len - 1:
                if list1[projected_skip] < list2[ptr2]:
                    ptr1 = projected_skip
                else:
                    ptr1 += 1
            else:
                ptr1 += 1
        else:
            # check for skip_pointer in list2
            projected_skip = ptr2 + list2_skip
            if ptr2 % list2_skip == 0 and projected_skip < list2_len - 1:
                if list2[projected_skip] < list1[ptr1]:
                    ptr2 = projected_skip
                else:
                    ptr2 += 1
            else:
                ptr2 += 1
    return result


def merge_or(list1, list2):
    result = []
    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(list1) and ptr2 < len(list2):
        if list1[ptr1] == list2[ptr2]:
            result.append(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif list1[ptr1] < list2[ptr2]:
            result.append(list1[ptr1])
            ptr1 += 1
        else:
            result.append(list2[ptr2])
            ptr2 += 1
    while (ptr1 < len(list1)):
        result.append(list1[ptr1])
        ptr1 += 1
    while (ptr2 < len(list2)):
        result.append(list2[ptr2])
        ptr2 += 1
    return result
