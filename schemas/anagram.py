from pydantic import BaseModel


class AnagramScheme(BaseModel):
    f_word: str
    s_word: str


class AnagramResponseScheme(BaseModel):
    status: bool = False
    counter: int
