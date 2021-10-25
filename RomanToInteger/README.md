# LeetCode - Python Practice
## Roman To Integer
#### https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

<pre>
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

<pre>
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
</pre>


Given a roman numeral, convert it to an integer.

 
<pre>
<strong>Example 1:</strong>
Input: s = "III"
Output: 3

<strong>Example 2:</strong>
Input: s = "IV"
Output: 4

<strong>Example 3:</strong>
Input: s = "IX"
Output: 9

<strong>Example 4:</strong>
Input: s = "LVIII"
Output: 58

<strong>Explanation:</strong> 
L = 50, V= 5, III = 3.

<strong>Example 5:</strong>
Input: s = "MCMXCIV"
Output: 1994

<strong>Explanation:</strong> 
M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<pre>
<strong>Constraints:</strong>

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
</pre>
