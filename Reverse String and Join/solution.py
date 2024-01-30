# def is_palindrome(num):
#     return str(num) == str(num)[::-1]
#
#
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
#
# def has_even_digits(num):
#     return all(int(digit) % 2 == 0 for digit in str(num))
#
#
# def has_odd_digits(num):
#     return any(int(digit) % 2 != 0 for digit in str(num))
#
#
# def generate_palindromic_primes(N):
#     palindromic_primes = []
#     num = 2
#     while len(palindromic_primes) < N:
#         if is_palindrome(num) and is_prime(num):
#             palindromic_primes.append(num)
#         num += 1
#     return palindromic_primes
#
#
# def filter_digits_and_print(palindromic_primes):
#     even_digit_numbers = [num for num in palindromic_primes if
#                           has_even_digits(num) and not has_odd_digits(num) and num != 2]
#     odd_digit_numbers = [num for num in palindromic_primes if not has_even_digits(num) and has_odd_digits(num)]
#
#     print(f"Palindromic primes with even digits: {len(even_digit_numbers)}")
#     print(f"Palindromic primes with odd digits: {len(odd_digit_numbers)}")
#
#
# # Take user input for N
# N = int(input("Enter the value of N: "))
#
# # Check for valid N
# if N < 0:
#     print("Please enter a non-negative integer for N.")
# elif N == 0:
#     print("No palindromic primes to generate for N = 0.")
# else:
#     palindromic_primes_list = generate_palindromic_primes(N)
#     filter_digits_and_print(palindromic_primes_list)
#
#
# # Function to check if Chef can reach CODETOWN
# # Function to check if Chef can reach CODETOWN
# def can_reach_codetown(s):
#     vowels = set("AEIOU")
#     codetown = "CODETOWN"
#
#     for i in range(8):
#         if s[i] != codetown[i]:
#             if (s[i] in vowels and codetown[i] in vowels) or (s[i] not in vowels and codetown[i] not in vowels):
#                 continue
#             else:
#                 return "NO"
#
#     return "YES"
#
#
# t = int(input())
#
# for _ in range(t):
#     s = input().upper()
#
#     result = can_reach_codetown(s)
# print(result)
for _ in range(int(input())):
    cost = 0
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(1, n - 1):
        if n < 3:
            if (a[i] == a[i - 1]):
                cost = cost + max(b[i], b[i - 1])
            else:
                cost = b[i] + b[i - 1]
        else:
            if (a[i] == a[i - 1]):
                cost = cost + max(b[i], b[i - 1])
            else:
                cost = cost + b[i]
    print(cost)
