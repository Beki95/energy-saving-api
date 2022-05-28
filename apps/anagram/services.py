import random


async def quick_sort(word):
    if len(word) <= 1:
        return word
    else:
        q = random.choice(word)
        left, right, middle = '', '', ''
        for elem in word:
            if elem < q:
                left += elem
            elif elem > q:
                right += elem
            else:
                middle += elem
    return await quick_sort(left) + middle + await quick_sort(right)
