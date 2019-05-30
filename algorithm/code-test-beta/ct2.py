from collections import Counter

def unitizeVectors(vector):
    [x, y] = vector
    if x == 0 and y == 0:
        return [0, 0]
    elif x == 0 and y > 0:
        return [0, 1.0]
    elif x == 0 and y < 0:
        return [0, -1.0]
    elif y == 0 and x > 0:
        return [1.0, 0]
    elif y == 0 and x < 0:
        return [-1.0, 0]
    elif x > 0:
        return [1.0, y/x]
    elif x < 0:
        return [-1.0, y/x]
    
def stringfyVectors(vector):
    [x, y] = vector
    [rx, ry] = unitizeVectors([x, y])
    return str(rx) + '_' + str(ry)


def solution(monsters, bullets):
    mon_vectors = [stringfyVectors([x, y]) for x, y in monsters]
    mon_vector_count = Counter(mon_vectors)
    hit = 0
    
    for b in bullets:
        b_vector = stringfyVectors(b)
        if mon_vector_count[b_vector] > 0:
            hit += 1
            mon_vector_count[b_vector] -= 1

    if hit == 0:
        hit = -1
        
    return hit