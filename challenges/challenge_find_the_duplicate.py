import collections


def find_duplicate(nums):
    if (
        not nums
        or len(nums) < 2
        or len(nums) == 2
        and not nums[0] == nums[1]
        or nums[0] < 0
    ):
        return False
    duplicate = [
        item for item, count in collections.Counter(nums).items() if count > 1
    ]
    return duplicate[0]


# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

# teste = [1, 3, 4, 2, 2]
# print(find_duplicate(teste))
