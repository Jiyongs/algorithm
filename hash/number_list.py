
# link : https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
# my answer : 효율성 테스트 TC 2개 시간초과
def solution(phone_book):
    phone_book = sorted(phone_book)
    for p in phone_book:
        for pp in phone_book:
            if p!=pp and p==pp[:len(p)]:
                    return False
    return True

 # other answer
def solution2(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# other answer (using hash)
def solution3(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True

if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421", "1111"]
    solution(phone_book)