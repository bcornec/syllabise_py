#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""Preprocess."""
import re
import file as fl
import sys

DICT_CONST = fl.open_yml('./constants.yaml')
VOWEL = DICT_CONST['vowel']
NO_E_VOWEL = VOWEL.copy()
NO_E_VOWEL.remove('e')
EXEPTION = DICT_CONST['exeption']
CONSONNANT = DICT_CONST['consonnant']


def list_letters_and_exceptions(word):
    """Return

    :param word: a word
    :type word: str
    :return: list of
    :rtype: list()
    """
    letters_and_exceptions = []
    w = word
    jump = 0
    for j in range(len(w)):
        if jump == 0:
            k = 0
            while True:
                if k != 0:
                    wj = w[j:-k]
                else:
                    wj = w[j:]
                if wj in EXEPTION:
                    jump = len(wj) - 1
                    letters_and_exceptions.append(wj)
                    break
                elif len(wj) == 1:
                    letters_and_exceptions.append(wj)
                    break
                elif wj == '':
                    break
                k += 1
        else:
            jump -= 1
    return letters_and_exceptions


def transform_cv(list_let_exc):
    """Return

    :param word: a word
    :type word: str
    :return: list of
    :rtype: list()
    """
    return [EXEPTION[let_exc] if let_exc in EXEPTION else
            'V' if let_exc in VOWEL else
            'C' if let_exc in CONSONNANT else ""
            for let_exc in list_let_exc]


def get_syllabe_cv(list_cv):
    """Return

    :param word: a word
    :type word: str
    :return: list of
    :rtype: list()
    """
    temp = [''.join(x) for x in re.findall(r'C*VC*', ''.join(list_cv))]
    syllabe_cv = []
    for i, x in enumerate(temp):
        if i != len(temp) - 1 and x[-1] == "C" and temp[i + 1][0] == "V":
            syllabe_cv.append(x[:-1])
            temp[i + 1] = "{}{}".format("C", temp[i + 1])
        else:
            syllabe_cv.append(x)
    return syllabe_cv


def get_syllabe(syllabe_cv, list_let_exc):
    """Return

    :param word: a word
    :type word: str
    :return: list of
    :rtype: list()
    """
    return [[list_let_exc.pop(0) for _ in range(len(scv))]
            for scv in syllabe_cv]


def syllabise_word(word):
    """Return

    :param word: a word
    :type word: str
    :return: list of
    :rtype: list()
    """
    list_let_exc = list_letters_and_exceptions(word)
    list_cv = transform_cv(list_let_exc)
    syllabe_cv = get_syllabe_cv(list_cv)
    d = []
    for c in syllabe_cv:
        e = []
        for _ in range(len(c)):
            e.append(list_let_exc.pop(0))
        d.append("".join(e))
    return d


def main():
    if len(sys.argv) == 1:
        print('usage: ./syllabe.py WORD [WORD [...]]')
    else:
        argv = sys.argv[1:]
        for words in argv:
            for word in words.split():
                print('{} => {}'.format(word, str(syllabise_word(word))))
    return 0


if __name__ == '__main__':
    main()
