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