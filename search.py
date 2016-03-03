import os
import getopt
import sys
import nltk
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import *
from sets import Set
from shunting_yard import *
from merge import *


def search_index(dictionary_file, postings_file, queries_file, output_file):
    dictionary = pickle.load(open(dictionary_file, 'rb'))
    postings_list = open(postings_file, 'r')
    query_list = open(queries_file, 'r').read().split("\n")
    # To remove the last '' item
    query_list.pop()
    search_results = open(output_file, 'w')

    for query in query_list:
        query_obj = get_query_obj(query, dictionary)
        return process_query_obj(query_obj, dictionary, postings_list)


def process_query_obj(query_obj, dictionary, postings_list):
    if isinstance(query_obj, Word):
        term = query_obj.value
        if term in dictionary:
            freq = dictionary[term][0]
            pointer = dictionary[term][1]
            results_list = get_results_list(freq, pointer, postings_list)
            if query_obj.is_not:
                results_list = merge_not(results_list)
            return results_list
        elif query_obj.is_not:
            # return full postings list of all doc IDs

    elif isinstance(query_obj, Query):
        postings_list1 = process_query_obj(query_obj.value1)
        postings_list2 = process_query_obj(query_obj.value2)
        return merge(postings_list1, postings_list2, query.op, query.is_not)


def get_results_list(freq, pointer, postings_list):
    postings_list.seek(pointer)
    results_list = postings_list.read(freq * 15 - 1).split(" ")
    results_list.pop()
    results_list = map((lambda x: int(x, 2)), results_list)
    return results_list


def usage():
    print "usage: " + sys.argv[0] + " -d dictionary-file -p postings-file -q file-of-queries -o output-file-of-results"

input_file_d = input_file_p = input_file_q = output_file = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:p:q:o:')
except getopt.GetoptError, err:
    usage()
    sys.exit(2)
for o, a in opts:
    if o == '-d':
        input_file_d = a
    elif o == '-p':
        input_file_p = a
    elif o == '-q':
        input_file_q = a
    elif o == '-o':
        output_file = a
    else:
        assert False, "unhandled option"
if input_file_d is None or input_file_p is None or input_file_q is None or output_file is None:
    usage()
    sys.exit(2)

search_index(input_file_d, input_file_p, input_file_q, output_file)
