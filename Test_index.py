# Number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input string
    s = input()
    
    # Initialize even and odd strings
    even_chars = ""
    odd_chars = ""
    
    # Iterate through the characters of the input string
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]
    
    # Print the even and odd characters separated by a space
    print(even_chars, odd_chars)
