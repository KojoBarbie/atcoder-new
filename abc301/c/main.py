"""

"""

import sys
from collections import Counter

def main():
    S = input()
    T = input()

    # 全文字を分けてカウントする
    s_counts = Counter(S)
    t_counts = Counter(T)

    if s_counts['@'] == 0 and t_counts['@'] == 0:
        if s_counts != t_counts:
            print("No")
        else:
            print("Yes")
        sys.exit()

    # a, t, c, o, d, e, r と @ を除去する
    replace_chars = 'atcoder'
    for c in replace_chars + '@':
        del s_counts[c]
        del t_counts[c]

    # 置き換え可能な文字とそれ以外の文字のカウントが一致する場合にイカサマができる
    if s_counts == t_counts:
        print("Yes")
    else:
        print("No")


main()