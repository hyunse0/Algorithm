# 프로그래머스 방금그곡

def change(string):
    string = list(string)

    i = 0
    while i < len(string):
        if string[i] == '#':
            string[i-1] = string[i-1].lower()
            string.pop(i)
        else:
            i += 1
    
    return ''.join(string)


def solution(m, musicinfos):
    answer = []
    
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        music = change(music)
        
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        during = (eh*60 + em) - (sh*60 + sm)
        
        total_music = music
        while len(total_music) < during:
            total_music += music
        
        total_music = total_music[:during]
        
        if change(m) in total_music:
            answer.append([during, (sh*60 + sm), title])
    
    if answer:
        answer.sort(key=lambda x: (-x[0], x[1]))
        return answer[0][2]
        
    return '(None)'


# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))