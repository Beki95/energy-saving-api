from fastapi import APIRouter
from fastapi import Depends

from apps.anagram.utils import Check, Checker, Count, Counter
from schemas.anagram import AnagramResponseScheme

anagram_router = APIRouter()


@anagram_router.post("/", response_model=AnagramResponseScheme)
async def checking_for_anagram(checker: Check = Depends(Checker),
                               counter: Count = Depends(Counter)):
    status = await checker()
    counter = await counter(status=status)
    return AnagramResponseScheme(status=status, counter=counter)
