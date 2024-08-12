def two_sums(nums, target):
    for i in nums:
        for j in nums:
            num = target - i
            numm = target - j
        if num in nums:
            return [[num, i], [numm, j]]
print(two_sums([6, 3, 4, 4, 6, 7, 8], 10))
[[6, 6], [4, 8]]



def int_toRoman(num):
    n = {"I" : 1, 
        "IV" : 4, "V" : 5,
        "IX" : 9, "X" : 10,
        "XL" : 40, "L" : 50,
        "XC" : 90, "C" : 100,
        "CD" : 400, "D" : 500,
        "CM" : 900, "M" : 1000}
    number = []
    for key, val in reversed(n.items( )):
        while num > 0:
            if val <= num:
                number.append(key)
                num -= val
            else:
                break
    return "".join(number)
print(int_toRoman(58))
