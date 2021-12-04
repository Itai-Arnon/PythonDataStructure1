import random


def unsort_if_same(words):
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)
    li2 = []
    for length, word in t:
        li2.append(word)
    for i in range(len(li2)):
        #range j run from i+1 to be efficient
        for j in range(i+1, len(li2)):
            if len(li2[i]) == len(li2[j]):
                pos = int(random.random()*(len(li2)))
                print(pos)
                li2[pos], li2[j] = li2[j], li2[pos] #swap has to occur
            else:
                continue
    return li2


word_lst = ['tami445', 'tami446', 'tami448', 't', 'tami448', 'tami447']
word_lst = unsort_if_same(word_lst)
print(word_lst)
