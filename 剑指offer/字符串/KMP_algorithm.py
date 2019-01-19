def kmp(s, t):
    n = len(s)
    m = len(t)

    pre_tab = processTab(t) # 预处理得到失配表
    # 失配表表示待匹配字符串在位置i失配时，i对应的字符应匹配的模板串j对应的字符

    j = 0 # j表示模板串t当前待匹配位置

    ans = -1
    found = 0

    for i in range(n):
        # i表示待匹配串s当前位置
        while (s[i] != t[j] and j != 0):
            # 当不匹配时，转移
            # 若 不加 j!= 0 则第一次不匹配会导致死循环
            # 当 j==0 或者 s[i] == t[j]时，会跳出循环
            j = pre_tab[j]

        if s[i] == t[j]:
            # 匹配的时候j后移
            j += 1;

        if j == m:
            # 找到了
            ans = i - m + 1
            found = 1

        if found:
            break

    return ans

def processTab(t):
    n = len(t)

    pre_tab = [0 for i in range(n+1)]

    for i in range(1, n):
        j = pre_tab[i]

        while (t[i] != t[j] and j != 0):
            # 当不匹配时，用来回溯j
            j = pre_tab[j]  

        if t[i] == t[j]:
            pre_tab[i + 1] = j + 1

    return pre_tab

if __name__ == '__main__':
    print(kmp("aaaabababba", "ababb"))