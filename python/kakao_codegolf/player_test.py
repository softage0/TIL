import player
import player1

r1 = []
r2 = []
win_count = 0

for i in range(1000):
    h1 = player.show_me_the_hand(r2)
    h2 = player1.show_me_the_hand(r1)
    if h1 == h2:
        print('match %d of 1000: tie' % i)
        r = 0
        win_count += 1
    elif (h1 == 'gawi' and h2 == 'bo') or (h1 == 'bawi' and h2 == 'gawi') or (h1 == 'bo' and h2 == 'bawi'):
        print('match %d of 1000: p1 win' % i)
        r = 1
        win_count += 3
    else:
        print('match %d of 1000: p2 win' % i)
        r = -1
    r1.insert(0, (h1, r))  # NOTE: 어제와 달라졌습니다!!!
    r2.insert(0, (h2, -r))  # NOTE: 어제와 달라졌습니다!!!
    # blah blah ...

print(win_count)
