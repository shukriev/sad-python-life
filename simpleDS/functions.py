def search_for_vowels(word: str) -> str:
    """Return any vovels found in a supplied word."""
    vowels = set('aeiou')
    print('something')
    return vowels.intersection(word)


def search_for_vowels(phrase: str, letters: str = 'def') -> str:
    return set(letters).intersection(set(phrase))


print(search_for_vowels('zasd'))

print(search_for_vowels('asd', 'dsaf'))
