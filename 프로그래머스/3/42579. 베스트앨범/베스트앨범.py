# 장르 높은 -> 노래 높은 -> 고유 번호 낮은 순
def solution(genres, plays):
    answer = []
    genres_total = {}

    genres_plays = [[genres[i], plays[i], i] for i in range(len(genres))]
    genres_plays = sorted(genres_plays, key=lambda x: (x[0], -x[1], x[2]))
    # print(genres_plays)

    for genre in genres_plays:
        if genre[0] not in genres_total:
            genres_total[genre[0]] = genre[1]
        else:
            genres_total[genre[0]] += genre[1]
    genres_total = sorted(genres_total.items(), key=lambda x:-x[1])
    # print(genres_total)
    for i in genres_total:
        count = 0
        for j in genres_plays:
            if i[0] == j[0]: # genre가 같다면
                count += 1
                if count <= 2:
                    answer.append(j[2])
                else:
                    break
    
    return answer