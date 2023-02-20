# WAPP to input n elements to a list, search an element using binary search technique.

listt = []
print("Enter Numbers: ")
for i in range(10):
    listt.insert(i, int(input()))
print("Enter a Number to search: ")
s_num = int(input())
start = 0
end = 9
# middle = (start+end)/2
# middle = int(middle)
while start <= end:
    middle = int((start+end)/2)

    if s_num < listt[middle]:
        end = middle - 1
    
    elif s_num > listt[middle]:
        start = middle + 1

    else:
        print("Number found at position: ", middle)
        break


if start > end:
    print("Number not found")