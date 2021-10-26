# Solution Explanation

### NOTE: This solution isn't working yet. I'm getting errors related to the indexing of the list

1. In order to "map" roman numerals <em>(I will refer to them as "numerals")</em> to their integer counterparts I created a dictionary for the standard numerals

<pre>
roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
</pre>
2. To handle the edge case where a smaller numeral precedes a larger numeral I use the following code:

<pre>
if roman_dict[prev] < roman_dict[next]:
            num += roman_dict[next] - roman_dict[prev]
</pre>

3. The roman numeral that is input is converted into a list so that I can check each roman numeral against the dictionary

<pre>
numeral_list = list(roman_numeral.upper())
</pre>

4. Then I iterate over the list checking if the previous list element is smaller than the next and making the appropriate conversion before adding it to the integer total

<pre>
def convert_to_int(roman_numeral):
    numeral_list = list(roman_numeral.upper())
    num = 0
    index = 1

    # Check each element in the list
    for numeral in numeral_list:
        prev = numeral
        next = numeral_list[index]

        # If the value of the previous element is less than the value of the next element subtract previous from next and add it to the integer (num)
        if roman_dict[prev] < roman_dict[next]:
            num += roman_dict[next] - roman_dict[prev]

        # Otherwise just add the value of the element to the integer (num)
        else:
            num += roman_dict[numeral]

        index += 1
        if index > (len(numeral_list) - 1):
            break

    print(num)
</pre>