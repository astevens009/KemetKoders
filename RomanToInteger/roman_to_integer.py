def convert_to_int(roman_numeral):
    numeral_list = list(roman_numeral.upper())
    # store the converted number
    num = 0
    index = 0           # index of the previous list element
    next_index = index  # index of the next list element
    # convert the Roman number into an integer
    for n in numeral_list:
        next_index += 1
        if next_index == len(numeral_list):
            break
        else:
            val = roman_dict[n]
            next_val = roman_dict[numeral_list[next_index]]

            if val < next_val:
                num += next_val - val
            else:
                num += val;

            index += 1

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
