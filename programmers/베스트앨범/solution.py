// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict

def solution(genres, plays):
    answer = defaultdict(list)
    res = []

    for i in range(len(genres)):
        if len(answer[genres[i]]) > 0:
            answer[genres[i]][0] += plays[i]
            answer[genres[i]][1].append((i,  plays[i]))      
        else:
            time = plays[i]
            songs = [(i, plays[i])]
            answer[genres[i]] = [time,  songs]

    answer = sorted(answer.items(), key=lambda x: -x[1][0])
    for t_time, (_, candits) in answer:
        cnt = 0
        candits = sorted(candits, key=lambda x: (-x[1], x[0]))
        while cnt < 2 and cnt < len(candits):
            res.append(candits[cnt][0])
            cnt += 1

    return res