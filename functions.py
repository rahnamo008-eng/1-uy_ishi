def hello():
    return "Hello, World!"

def kvadrat(a):
    return a ** 2

def kub(a):
    return a ** 3


def yigindi(a, b):
    return a + b

def ayirma(a, b):
    return a - b

def kopaytma(a, b):
    return a * b

def bolish(a, b):
    if b != 0:
        return a / b
    return "Nolga bo'lish mumkin emas!"

def max_son(a, b):
    return a if a > b else b

def min_son(a, b):
    return a if a < b else b

def juftmi(a):
    return a % 2 == 0

def toqmi(a):
    return a % 2 != 0
def katta_harf(matn):
    return matn.upper()

def kichik_harf(matn):
    return matn.lower()

def teskari(matn):
    return matn[::-1]

def uzunligi(matn):
    return len(matn)

def yigindi_list(lst):
    jami = 0
    for son in lst:
        jami += son
    return jami

def eng_katta(lst):
    katta = lst[0]
    for son in lst:
        if son > katta:
            katta = son
    return katta

def eng_kichik(lst):
    kichik = lst[0]
    for son in lst:
        if son < kichik:
            kichik = son
    return kichik

def uzunligi_list(lst):
    element_soni = 0
    for i in lst:
        element_soni += 1
    return element_soni
def faktorial(n):
    if n == 0 or n == 1:
        return 1
    p_kopaytma = 1
    for i in range(1, n + 1):
        p_kopaytma = p_kopaytma * i
    return p_kopaytma

def daraja(a, b):
    return a ** b

def abs_son(a):
    if a < 0:
        return -a
    else:
        return a


print(hello())
print(kvadrat(5))
print(kub(3))
print(yigindi(5, 7))
print(ayirma(10, 2))
print(kopaytma(3, 4))
print(bolish(20, 5))
print(max_son(4, 8))
print(min_son(4, 8))
print(juftmi(12))
print(toqmi(7))
print(katta_harf("python"))
print(kichik_harf("PYTHON"))
print(teskari("GitHub"))
print(uzunligi("Python"))
print(yigindi_list([1, 2, 3, 4]))
print(eng_katta([5, 7, 1, 9]))
print(eng_kichik([5, 7, 1, 9]))
print(uzunligi_list([1, 2, 3]))
print(faktorial(5))
print(daraja(2, 5))
print(abs_son(-15))