from itertools import combinations

# link : https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
# my answer : 일부 TC 시간초과
def solution(clothes):
    # [종류_명칭, 종류_명칭2, 종류2_명칭]
    temp_list = list(map(lambda x: x[1] + '|' + x[0], clothes))
    answer_list = []

    for type_cnt in range(len(set(list(map(lambda x:x[0], clothes))))):
        for result in list(combinations((temp_list),type_cnt+1)):
            temp = []
            is_in = False
            for r in result:
                temp_type = r.split("|")[0]
                if temp_type in temp:
                    is_in = True
                    break
                temp.append(temp_type)
            if is_in is False:
                answer_list.append(result)

    return len(answer_list)

# other answer
def solution2(clothes):
    clothes_type = {}
    for _, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 2
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num

    return cnt - 1


if __name__ == '__main__':
    clothes = [["crowmask", "test"], ["bluesunglasses", "face"], ["smoky_makeup", "face"], ["why", "test"]]
    solution(clothes)
