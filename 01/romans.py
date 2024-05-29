def int_to_roman(num):
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

    resultado = ''

    for i in range(len(val) - 1, -1, -1):
        while num >= val[i]:
            resultado += roman[i]
            num -= val[i]

    return resultado

print(int_to_roman(1024))

pass

def roman_to_int(s):
    num = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

    resultado = 0

    for i in range(len(s)):
        if i > 0 and num[s[i]] > num[s[i - 1]]:
            resultado += num[s[i]] - 2 * num[s[i - 1]]
        else:
            resultado += num[s[i]]

    return resultado

print(roman_to_int("X"))

pass
