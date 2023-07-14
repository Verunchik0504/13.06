# O (N**2)
'''
def strcounter(s):
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(f'{sym} - {counter}')'''


# O (2 * N) или O (N)
'''
def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    
    for sym, count in syms_counter.items():
        print(f'{sym} - {count}')


strcounter('zzzzzxcv')'''

a = str(input())
if a == a[::-1]:
    print('True')
else:
    print('False')