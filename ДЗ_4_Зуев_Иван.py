#1
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("Расстояние ", distance(2, 3, 4, 9))

#2    
def power(a, n):
    res = 1
    for i in range (abs(n)):
        res *= a
    if n < 0:
        res2 = 1 / res
        return res2
    return res

print(power(3, -3))
print(power(3, 3))

#3
sentence = input()

def capitalize(word):
    if len(word) == 0:
        return word

    return chr(ord(word[0]) - 32) + word[1:]

def capitalize_sentence(sentence):
    words = sentence.split()
    capitalized_words = [capitalize(word) for word in words]
    return ' '.join(capitalized_words)

print(capitalize_sentence(sentence))

#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

#5
def power(a, n):
    if n == 0:
        return 1
    if n > 0:
        return a * power(a, n-1)
    
print(power(23, 2))

#6
def prikol():
    a = int(input())
    if a == 0:
        return
    else:
        prikol()
        print(a)

print(prikol())



