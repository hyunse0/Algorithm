def solution(array, commands):
    answer = []

    for i, j, k in commands:
        cut_arr = array[(i-1):j]

        # 버블 정렬
        for x in range(len(cut_arr)-1, -1, -1):
            for y in range(0, x):
                if cut_arr[y] > cut_arr[y+1]:
                    cut_arr[y], cut_arr[y+1] = cut_arr[y+1], cut_arr[y]


        answer.append(cut_arr[k-1])

    return answer