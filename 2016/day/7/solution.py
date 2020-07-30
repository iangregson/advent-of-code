#!/usr/bin/env python3

import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

file = open(dir_path + "/input.txt", "r")
input_txt = [line.strip() for line in file.readlines()]

# input_txt = [
#     'abba[mnop]qrst',
#     'abcd[bddb]xyyx',
#     'aaaa[qwer]tyui',
#     'ioxxoj[asdfgh]zxcvbn',
#     'asdhjkbnmsdfjkh',
#     'lhhhlyioiiknkray[omilmxkodlmvzhkgbaf]cyftkgjpvjvdnortlj[ifljdtkgscmnmxsq]nxtettqnuaotfsh',
#     'uyiazdptoxzxbzo[bmuglholukatdbf]ascjhcllcatoapyvn[isqfrvbbkzsxixjuqrq]ncwzqqgudgwrtxvzfe[spqvftdlddlfglgg]zrqbukmufumytpc'
# ]

# input_txt = [
#     'aba[bab]xyz',
#     'xyx[xyx]xyx',
#     'aaa[kek]eke',
#     'zazbz[bzb]cdb',
# ]


def double_char_spans(s, pattern=r'([a-z])\1+'):
    results = []
    matches = re.finditer(pattern, s)
    for m in matches:
        results.append(m.span())
    return results


def hypernet_spans(s, pattern=r'\[(.*?)\]'):
    results = []
    matches = re.finditer(pattern, s)
    for m in matches:
        results.append(m.span())
    return results


def has_ABBA(s):
    dcis = double_char_spans(s)
    if len(dcis) == 0:
        return False

    has_valid_dci = False
    for dci in dcis:
        if dci[0] <= 0:
            has_valid_dci = False
            continue
        if dci[1] >= len(s):
            has_valid_dci = False
            continue

        prefix_is_valid = s[dci[0]-1] != s[dci[0]]
        suffix_is_valid = s[dci[1]-1] != s[dci[1]]
        if prefix_is_valid and suffix_is_valid:
            has_valid_dci = s[dci[0]-1] == s[dci[1]]
        else:
            has_valid_dci = False

        if dci[1] - dci[0] != 2:
            has_valid_dci = False

        if has_valid_dci == True:
            break

    return has_valid_dci


results = []
for idx, line in enumerate(input_txt):
    if not has_ABBA(line):
        results.append(0)
        continue

    hs = hypernet_spans(line)
    if len(hs) > 0:
        has_hypernet_span = False
        for h in hs:
            if has_ABBA(line[h[0]:h[1]]):
                has_hypernet_span = True
        if has_hypernet_span == True:
            results.append(0)
            continue

    results.append(1)

print("Part 1 answer:", sum(results))


def has_ABA(ss):
    sss = re.split(r'\[.*?\]+', ss)
    abas = []
    for s in sss:
        i = 0
        j = i + 2
        while j < len(s):
            if s[i] == s[j] and s[i+1] != s[j]:
                abas.append(s[i:j+1])
            i += 1
            j += 1

    if len(abas) == 0:
        return False

    return abas


def has_BAB(s, aba):
    bab = "".join([aba[1], aba[0], aba[1]])
    hs = hypernet_spans(s)
    for hs in hs:
        if bab in s[hs[0]:hs[1]]:
            return True

    return False


results = []
for line in input_txt:
    if has_ABA(line) == False:
        results.append(0)
        continue

    has_bab = False
    for aba in has_ABA(line):
        if has_BAB(line, aba):
            has_bab = True
            break

    if has_bab == True:
        results.append(1)
        continue

print("Part 2 answer:", sum(results))
