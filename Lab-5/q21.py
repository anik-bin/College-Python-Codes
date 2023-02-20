# WAP to generate the pascal triangle pyramid of numbers for a given number. Ex. for number 4
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

def pattern_print(n):
    row = [1]
    print(*row)
    for i in range(1, n):
        next_row = [1]
        for j in range(1, i):
            next_row.append(row[j-1] + row[j])
        next_row.append(1)
        print(*next_row)
        row = next_row
n=int(input("Enter number of rows : "))
pattern_print(n)