# anagram
# def anagramSolution1(s1,s2):
#     alist = list(s2)
#
#     pos1 = 0
#     stillOK = True
#
#     while pos1 < len(s1) and stillOK:
#         pos2 = 0
#         found = False
#         while pos2 < len(alist) and not found:
#             if s1[pos1] == alist[pos2]:
#                 found = True
#             else:
#                 pos2 = pos2 + 1
#
#         if found:
#             alist[pos2] = None
#         else:
#             stillOK = False
#
#         pos1 = pos1 + 1
#
#     return stillOK
#
# print(anagramSolution1('abcd','dcbao'))

# def check_anagrams(s1, s2):
#     alist = list(s2)
#     position = 0
#     anagram = True
#
#     while position < len(s1) and anagram:
#         position2 = 0
#         found = False
#         while position2 <len(alist) and not found:
#             if s1[position] == alist[position2]:
#                 found = True
#             else:
#                 position2 +=1
#         if found:
#             alist[position2] = None
#         else:
#             anagram = False
#         position += 1
#     return anagram



from collections import Counter

def check_anagrams(first_word, second_word):
	if Counter(first_word) == Counter(second_word):
		return 1
	else:
		return 0


firstWords = 'cinema', 'host', 'aba', 'train'
secondWords = 'iceman', 'shot', 'bab', 'rain'

for pair in zip(firstWords, secondWords):
	print check_anagrams(*pair)




# print(check_anagrams(["iceman","host", "aba", "train"], ["cinema", "shot", "bab", "rain"]))
