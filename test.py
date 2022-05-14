nums = [1, 2, [], 3, [[]], [4]]

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


print(list(flatten(nums)))