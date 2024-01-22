def register(users, emoticons, cur_rates):
    registered = 0
    total = 0
    for rate_bnd, price_bnd in users:
        accum = 0
        for rate, price in zip(cur_rates, emoticons):
            if rate >= rate_bnd:
                accum += (100 - rate) * price // 100
        if accum >= price_bnd:
            registered += 1
        else:
            total += accum
    return registered, total

def DFS(users, emoticons, eid, cur_rates=[]):
    """
    Input: (`users`, `emoticons`, current emoticon index, current discount rates)
    Return: (# of regist., accum.)
    """
    DISCOUNT = [10, 20, 30, 40]
    
    if eid == len(emoticons):
        return register(users, emoticons, cur_rates)
    
    results = []
    for rate in DISCOUNT:
        results.append(DFS(users, emoticons, eid+1, [*cur_rates, rate]))
    
    max_reg = 0
    max_accum = None
    for reg, accum in results:
        if reg > max_reg:
            max_reg = reg
            max_accum = accum
        elif reg == max_reg:
            if max_accum is None or accum > max_accum:
                max_accum = accum
    
    return [max_reg, max_accum]

def solution(users, emoticons):
    emoticons = sorted(emoticons, reverse=True)
    
    return DFS(users, emoticons, 0)