def fizzbizz(nums):
    result = []
    for num in range(1,nums+1):
        if num % 15 == 0:
            result.append("FizzBizz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Bizz")
        else:
            result.append(num)
    return result

if __name__ == '__main__':
    print(fizzbizz(15))