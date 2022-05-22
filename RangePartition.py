T = int(input())
for iiiii in range(T):
    n, x, y = map(int, input().split())
    
    su = (n * (n+1)) // 2
    if su %(x+y) != 0:
        k = 'IM'
        print(f'Case #{iiiii+1}: IMPOSSIBLE')
        continue
    tar = su * (x) // (x+y)
    ans = []
    for i in range(n, -1, -1):
        if tar > i:
            tar -= i
            ans.append(i)
        elif tar <= i:
            ans.append(tar)
            break
    print(f'Case #{iiiii+1}: POSSIBLE')
    print(f'{len(ans)}')
    print(f'{" ".join(map(str, ans))}')