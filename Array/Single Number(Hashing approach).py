#Hashing approach
def getSingleElement(arr):
    # Size of the array:
    n = len(arr)

    # Find the maximum element:
    maxi = max(arr)

    # Declare hash array of size maxi+1
    # And hash the given array:
    hash = [0] * (maxi + 1)
    for num in arr:
        hash[num] += 1

    # Find the single element and return the answer:
    for num in arr:
        if hash[num] == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1


def main():
    arr = [4, 1, 2, 1, 2]
    ans = getSingleElement(arr)
    print("The single element is:", ans)


if __name__ == '__main__':
    main()
