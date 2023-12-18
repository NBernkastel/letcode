senate = "DDRRRR"


def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    rad_queue = []
    dir_queue = []
    for i in range(len(senate)):
        if senate[i] == 'R':
            rad_queue.append(i)
        else:
            dir_queue.append(i)
    while rad_queue and dir_queue:
        if rad_queue[0] < dir_queue[0]:
            rad_queue.pop(0)
            rad_queue.append(n)
            dir_queue.pop(0)
            n += 1
        else:
            dir_queue.pop(0)
            dir_queue.append(n)
            rad_queue.pop(0)
            n += 1
    if rad_queue:
        return 'Radiant'
    else:
        return 'Dire'


print(predictPartyVictory(senate))
