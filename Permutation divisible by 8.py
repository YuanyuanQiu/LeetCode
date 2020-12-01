'''
Question: Given a large number N and the task is to check if any permutation
of a large number is divisible by 8.
Answer: if the last three digits of a number are divisible by 8, then the
number is also divisible by 8'''
def solve(n, l):      
    # Less than three digit number can be checked directly. 
    if l < 3: 
        if int(n) % 8 == 0: 
            return True
        # check for the reverse of a number 
        n = n[::-1]
        if int(n) % 8 == 0: 
            return True
        return False
  
    # Stores the Frequency of characters in the n. 
    hash = 10 * [0] 
    for i in range(0, l): 
        hash[int(n[i])] += 1; 
  
    # Iterates for all three digit numbers divisible by 8 
    for i in range(104, 1000, 8):
        # print(i)
        dup = i
  
        # stores the frequency of all single digit in three-digit number 
        freq = 10 * [0]
        # ones place
        freq[int(dup % 10)] += 1; 
        # tens place
        dup = dup / 10
        freq[int(dup % 10)] += 1;
        # hundreds place
        dup = dup / 10
        freq[int(dup % 10)] += 1; 
          
        dup = i 
        
        # check if the original number has the digit:
        # if not, continue, if yes, return True
        # ones place
        if (freq[int(dup % 10)] > hash[int(dup % 10)]): 
            continue; 
        # tens place
        dup = dup / 10; 
        if (freq[int(dup % 10)] > hash[int(dup % 10)]): 
            continue; 
        # hundreds place
        dup = dup / 10
        if (freq[int(dup % 10)] > hash[int(dup % 10)]): 
            continue; 
          
        return True
  
    # when all are checked its not possible 
    return False
      
# Driver Code 
if __name__ == "__main__":   
    number = "9104"
    l = len(number) 
    if solve(number, l): 
        print("Yes") 
    else: 
        print("No") 