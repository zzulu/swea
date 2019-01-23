def palindrome(s):
    if len(s) < 2 or s[0] == '*' or s[-1] == '*':
        return 'Exist'
    if s[0] != s[-1]:
        return 'Not exist'
    return palindrome(s[1:-1])

for t in range(int(input())):
    print(f'#{t+1} {palindrome(input())}')