def solution(bandage, health, attacks):
    time, heal, bonus = bandage
    max_health = health
    max_tick = attacks[-1][0]
    tick = -1
    i, j = 0, 0
    while health > 0 and tick < max_tick:
        tick += 1
        
        if tick == attacks[j][0]:   # 피격된 경우
            health -= attacks[j][1] # 체력 감소
            j += 1
            i = 0
            continue
        
        health += heal
        i += 1
        
        if i == time:
            i = 0
            health += bonus
            
        if health > max_health: # 최대체력 이상인 경우
            health = max_health
        # 1초마다 heal 만큼 체력 회복
        # 만약 피격시 회복 중단 (피격된 초는 회복하지 않음)
        
    return (health if health > 0 else -1)