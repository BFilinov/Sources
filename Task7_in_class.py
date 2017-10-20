def is_palindrome(s):
    from functools import reduce
    s_trim = list(filter(lambda char: char != ' ', s))
    checksum = [ord(s_trim[i]) - ord(s_trim[-i]) for i in range(len(s_trim) // 2)]
    return reduce(lambda x, y: x + y, checksum) == 0


print(is_palindrome('а роза упала на лапу азора'))
print(is_palindrome('not a palindrome'))
