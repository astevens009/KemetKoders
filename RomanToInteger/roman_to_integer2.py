def convert_to_int(roman_numeral):
    numeral_list = list(roman_numeral.upper())
    num = 0
    index = 1

    for numeral in numeral_list:
        prev = numeral
        next = numeral_list[index]

        if roman_dict[prev] < roman_dict[next]:
            num += roman_dict[next] - roman_dict[prev]
        else:
            num += roman_dict[numeral]

        index += 1
        if index > (len(numeral_list) - 1):
            break

    print(num)


roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# roman_numeral = input("Please enter the Roman numeral: ").upper()

convert_to_int('mmxxi')     # 2021
convert_to_int('MMI')       # 2001
convert_to_int('ix')        # 9
convert_to_int('IV')        # 4
convert_to_int('XII')       # 12
