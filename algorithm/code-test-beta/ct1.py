def getToppingPositions(topping):
    t_pos = {}
    for i in range(len(topping)):
        if t_pos.get(topping[i]):
            t_pos[topping[i]].append(i)
        else:
            t_pos[topping[i]] = [i]
    
    return t_pos

def getDistance(start, end, t_len):
    if start > end:
        low = end
        high = start
    else:
        low = start
        high = end
        
    if high - low < t_len + low - high:
        return high - low
    else:
        return t_len + low - high

def getShorterDistance(cur_pos, distance_so_far, remain_taste, topping_len, topping_poses):
    t_pos = topping_poses[remain_taste[0]]
    dist0 = getDistance(cur_pos, t_pos[0], topping_len) + distance_so_far
    dist1 = getDistance(cur_pos, t_pos[1], topping_len) + distance_so_far
    
    if len(remain_taste) != 1:
        dist0 = getShorterDistance(t_pos[0], dist0, remain_taste[1:], topping_len, topping_poses)
        dist1 = getShorterDistance(t_pos[1], dist1, remain_taste[1:], topping_len, topping_poses)
        
    if dist0 < dist1:
        return dist0
    else:
        return dist1
    
    
def solution(topping, tasting):
    topping_len = len(topping)
    topping_poses = getToppingPositions(topping)
    pos = 0
    distance = 0
    
    return getShorterDistance(0, 0, tasting, topping_len, topping_poses)
