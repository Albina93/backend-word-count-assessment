
__author__ = "Albina Tileubergen-Thomas help from Chris Warren, Cheria Artis"

import sys
import re


def create_word_dict(filename):
    word_count = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                each_word = word.lower()
                if each_word in word_count:
                    word_count[each_word] += 1
                else:
                    word_count[each_word] = 1
    return word_count


def print_words(filename):
    word_dict = create_word_dict(filename)
    for item in sorted(word_dict):
        print(item, ":", word_dict[item])
    return word_dict


def print_top(filename):
    word_dict = create_word_dict(filename)
    top_twenty = sorted(word_dict, key=lambda item: -word_dict[item])[:20]
    for item in top_twenty:
        print(item + " : " + str(word_dict[item]))
    return word_dict


def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
