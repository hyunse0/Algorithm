# 프로그래머스 베스트앨범

from collections import defaultdict

def solution(genres, plays):
    album = defaultdict(list)
    for i in range(len(genres)):
        album[genres[i]].append((i, plays[i]))
    
    sorted_genres = sorted(album.keys(), key=lambda x: -sum(song[1] for song in album[x]))

    answer = []
    for genre in sorted_genres:
        songs = sorted(album[genre], key=lambda x: (-x[1], x[0]))
        
        answer.append(songs[0][0])
        if len(songs) > 1:
            answer.append(songs[1][0])
            
    return answer

genres = ['a','b','c','d','a','d','d','d','a','a','c','c']
plays = [100,300,400,150,100,300,200,600,700,110,900,9000]
print(solution(genres, plays))
