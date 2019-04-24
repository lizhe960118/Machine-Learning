def helper(n, p):
    all_money = 1.0
    xiaomi = 0.0
    xiaohua = 0.0
    flag = 1
    cur_index = 0
    step = 0
    spend = 0

    while step < 100:
        if spend + all_money * p[cur_index] > all_money:
            break

        if flag == 1:
            xiaomi += all_money * p[cur_index]
        else:
            xiaohua += all_money * p[cur_index]

        cur_index = (cur_index + 1) % n
        flag *= -1
        step += 1
        spend = xiaomi + xiaohua

    if step == 100:
       return 0.0

    if flag == 1:
        xiaomi = all_money - xiaohua
    else:
        xiaohua = all_money - xiaomi

    return xiaomi

if __name__ == '__main__':
    n = int(raw_input())
    p = []
    for i in range(n):
        p.append(float(raw_input()))
    xiaomi = helper(n, p)
    print ':.4f'.format(xiaomi)


