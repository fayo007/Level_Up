# Count the Digit   
# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

# Square all numbers k (0 <= k <= n) between 0 and n.

# Count the numbers of digits d used in the writing of all the k**2.

def nb_dig(n, d):
    p = ''

    for i in range(n+1):
        p += str(i**2)
    
    counts = p.count(str(d))

    return counts

print(nb_dig(10,0))