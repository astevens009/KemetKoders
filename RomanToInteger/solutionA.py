def evalRoman(romanNumberal) -> int:
    romanNumberalValues = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IX": 9,
        "IV": 4,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
 
    idx = 1
    last = romanNumberal[0]
    total = 0

    while idx < len(romanNumberal):
        current = romanNumberal[idx]

        # A pair was found previously so we need to iterate to get a new 'last' pointer
        if last == None:
            last = current
            idx += 1
            continue

        romanPair = last + current
        sum = romanNumberalValues.get(romanPair)
        pairFound = False

        # Iterate through the roman numberal string to find pairs
        # Use the roman numberal hash map to evalute each roman numberal values
        if sum == None:
            if(idx == len(romanNumberal) - 1):
                total += romanNumberalValues.get(current)
            total += romanNumberalValues.get(last)
        else:
            total += sum
            pairFound = True

        # Pair was found so we set the last pointer to None
        if pairFound:
            last = None
        else:
            last = current

        idx += 1

    return total
