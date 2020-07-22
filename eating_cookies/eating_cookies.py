'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)

# def eating_cookies_cache(n, cache={}):
    # if n < 2:
    #     return 1
    # elif n == 2:
    #     return 2
    # elif n == 3:
    #     return 4
    # elif n in cache:
    #     return cache[n]
    # else:
    #     # find all paths to 0 cookies
    #     one_cookie_eaten = eating_cookies(n - 1, cache)
    #     two_cookies_eaten = eating_cookies(n - 2, cache)
    #     three_cookies_eaten = eating_cookies(n - 3, cache)
    #     cache[n] = one_cookie_eaten + two_cookies_eaten + three_cookies_eaten
    #     return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


