def solution(phone_book):
    phone_book.sort()
    for pref in range(len(phone_book) - 1):
        if phone_book[pref + 1].startswith(phone_book[pref]):
            return False
    return True