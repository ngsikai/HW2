def merge(list1, list2, op, is_not):
	if (is_not):
		if (op == "AND"):
			return merge_not(merge_and(list1, list2))
		elif (op == "OR"):
			return merge_not(merge_or(list1, list2))
	else:
		if (op == "AND"):
			return merge_and(list1, list2)
		elif (op == "OR"):
			return merge_or(list1, list2)

def merge_not(list, list_all):
	# TO-DO
	return

def merge_and(list1, list2):
	result = []
	ptr1 = 0
	ptr2 = 0
	while ptr1 < len(list1) and ptr2 < len(list2):
		if list1[ptr1] == list2[ptr2]:
			result.append(list1[ptr1])
			ptr1 += 1
			ptr2 += 1
		elif list1[ptr1] < list2[ptr2]:
			ptr1 += 1
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

# first = [2, 4, 8, 16, 32, 64, 128]
# second = [1, 2, 3, 5, 8, 13, 21, 34]
# print merge_and(first, second)
# print merge_or(first, second)