#Approach
- Store all possible roman number values in a hash map for simple roman to integer evaluation. 
- Use two pointers(one for the previous position another for the current) while iterating through the roman string 
  starting at index 1
- While traversing the array the roman integer value is added to the total 
 - During this process I keep track if a pair was found because if so this indicates that the previous pointer 
    was already added to the total sum so we do nothing on the next iteration to aquire a new pointer.
    On the following iteration we continue searching for pairs
- finally the total sum is returned

**I did not test this algorithm extensively I only used the examples given within the readme**
