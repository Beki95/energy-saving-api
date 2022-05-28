from fastapi import APIRouter
from fastapi import Depends

from apps.anagram.services import quick_sort
from schemas.anagram import AnagramScheme, AnagramResponseScheme

anagram_router = APIRouter()


def checking_for_anagram(words: AnagramScheme) \
        -> AnagramResponseScheme:
    response = {'counter': 0}
    if quick_sort(words.f_word) == quick_sort(words.s_word):
        response['status'] = True
    return AnagramResponseScheme(**response)


@anagram_router.post("/", response_model=AnagramResponseScheme)
async def checking_for_anagram(check=Depends(checking_for_anagram)):
    return check
