T = input()
T = int(T)
for i in range(1, T+1):
    n = input()
    pa = input()
    up = False
    down = False
    dig = False
    spe = False
    for p in pa:
        if p.isalpha():
            if ord(p) >= 97:
                down = True
            else:
                up = True
        elif p.isdigit():
            dig = True
        elif p in '#@*&':
            spe = True
    if not up:
        pa += 'A'
    if not down:
        pa += 'a'
    if not dig:
        pa += '1'
    if not spe:
        pa += '#'
    while len(pa) < 7:
        pa += 'A'
    print(f'Case #{i}: {pa}')