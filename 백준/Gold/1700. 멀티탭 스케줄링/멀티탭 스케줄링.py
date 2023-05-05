from collections import deque
tap, l = map(int, input().split())
lst = deque(list(map(int, input().split())))
concent = [0 for _ in range(tap)]
cnt = 0
while lst:
    p = lst.popleft()
    if p in concent:
        continue

    elif 0 in concent:
        for idx, connected in enumerate(concent):
            if not connected:
                concent[idx] = p
                break
    
    else:
        flag = False
        for x, i in enumerate(concent):
            if i not in lst:
                flag = True
                concent[x] = p
                cnt += 1
                break
        
        if not flag:
            id_lst = [lst.index(i) for i in concent]
            concent[id_lst.index(max(id_lst))] = p
            cnt += 1
    
    # print(concent, cnt)
print(cnt)