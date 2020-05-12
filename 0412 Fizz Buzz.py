# def fizzBuzz(n):
#     ls = list(range(1,n+1))
#     for i in range(len(ls)):
#         if (i+1) % 3 == 0:
#             ls[i] = "Fizz"
#         if (i+1) % 5 == 0:
#             if ls[i] == "Fizz":
#                 ls[i] = "FizzBuzz"
#             else:
#                 ls[i] = "Buzz"
#         ls[i] = str(ls[i])
            
#     return ls

def fizzBuzz(n):
    # ans list
    ans = []

    for num in range(1,n+1):

        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)

        num_ans_str = ""

        if divisible_by_3:
            # Divides by 3
            num_ans_str += "Fizz"
        if divisible_by_5:
            # Divides by 5
            num_ans_str += "Buzz"
        if not num_ans_str:
            # Not divisible by 3 or 5
            num_ans_str = str(num)

        # Append the current answer str to the ans list
        ans.append(num_ans_str)  

    return ans

print(fizzBuzz(15))