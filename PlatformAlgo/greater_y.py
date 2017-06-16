#Write a program that takes an array and returns the number of values in that array whose value is greater than y. For example, if array = [1,3, 5, 7] and y = 3, after your program is run it will print 2 (since there are two values in the array whose value is greater than 3).  Again make sure you come up with a simple base case and write instructions to solve that base case first and then test your instructions for other complicated cases. You can use a count function with this assignment.

def greater_y(arr, y):
    count = 0
    for i in range(len(arr)):
        if arr[i] > y:
            count += 1
    return count


print(greater_y([1,3, 5, 7], 3))
