from collections import Counter

# link : https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
def solution(genres, plays):
    # {고유번호 : 재생횟수_장르} 형태로 재정의
    total = []
    nums = []
    for idx, v in enumerate(genres):
        total.append(str(plays[idx]) + "_" + v)
        nums.append(idx)
    albums = dict(zip(nums, total))

    # 딕셔너리 값(재생횟수_장르) 내림차순 정렬
    sort_albums_by_play = sorted(albums.items(), key=(lambda x: int(x[1].split("_")[0])), reverse=True)

    # 장르별 우선순위 얻기
    # (장르 : 재생횟수) 형태로 재정의
    genre_play = tuple(zip(genres, plays))
    genre_kind = {}
    for i in genre_play:
        genre_kind[i[0]] = genre_kind[i[0]] + i[1] if i[0] in genre_kind.keys() else i[1]
    # 재생횟수가 높은 순으로 장르 정렬
    # sorted(dict) : [(장르, 재생횟수총합)] 형태로 리턴
    sort_genre_kind = sorted(genre_kind.items(), key=(lambda x: x[1]), reverse=True)

    # 장르별 베스트 top2 노래 리턴
    answer = []
    answer_genres = {}
    for g in sort_genre_kind:
        gg = g[0]
        for a in sort_albums_by_play:
            # a : (3, '800_kpop')
                num = a[0]
                genre = a[1].split("_")[1]
                if gg == genre:
                    # 변수 = 값1 if 조건문 else2 : 조건문이 true면 값1 false면 값2
                    answer_genres[genre] = answer_genres[genre] + 1 if genre in answer_genres.keys() else 1
                    if(Counter(answer_genres)[genre]<3):
                        answer.append(num)
        answer_genres = {}

    return answer

# other answer
def solution2(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}  # d = {장르:[]}
    for e in zip(genres, plays, range(len(plays))): # zip : [[장르, 재생횟수, 고유번호], ...]
        d[e[0]].append([e[1] , e[2]]) # d = {장르:[[재생횟수, 고유번호], ...]}
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    solution(genres, plays)