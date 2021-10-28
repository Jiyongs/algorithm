
# link : https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# my answer1 : 효율성 테스트 4개 시간초과
def solution1(participant, completion):
    participant.sort()
    completion.sort()
    for c in completion:
        participant.remove(c)

    return participant[0]

# my answer2 : 통과
def solution2(participant, completion):
    p_dict = {}
    for p in participant:
        keys = p_dict.keys()
        p_dict[p] = p_dict[p]+1 if p in keys else 1
    c_dict = {}
    for c in completion:
        keys = c_dict.keys()
        c_dict[c] = c_dict[c]+1 if c in keys else 1

    for p in participant:
        if p not in c_dict.keys():
            return p
        if p_dict[p] != c_dict[p]:
            return p
    return 0

# other answer
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    solution2(participant, completion)
