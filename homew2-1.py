def check(skobkis):
    skobka = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in skobkis:
        if char in skobka:
            stack.append(char)
        elif not stack or skobka[stack.pop()] != char:
            return False

    return len(stack) == 0


a = '(({[]}))'
b1 = '{(})'
c = '([])[[]]'
b2 = ')())[[]]'
b3 = '(())[[]]'
b4 = '([])'

print(check(a))
print(check(b1))
print(check(c))
print(check(b2))
print(check(b3))
print(check(b4))