#! usr/bin/python

# A. Все перестановки заданной длины

def print_nums(nums: list[int]) -> None:
    print(*nums, sep='')


def generate(nums: list[int]) -> None:
    n = len(nums)
    while True:
        print_nums(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            return
        for j in range(n - 1, -1, -1):
            if nums[j] > nums[i]:
                break
        else:
            return
        nums[i], nums[j] = nums[j], nums[i]
        nums = nums[:i + 1] + nums[n - 1:i: -1]


def main():
    n = int(input())
    nums = [(i + 1) for i in range(n)]
    generate(nums)
    pass


if __name__ == '__main__':
    main()
