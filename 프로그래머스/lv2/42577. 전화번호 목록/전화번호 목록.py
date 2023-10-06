'''
Time Out
O(n^2)
'''
def solution1(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    while phone_book:
        prefix = phone_book.pop(0)
        for num_seq in phone_book:
            if prefix == num_seq[:len(prefix)]:
                return False
    return True

'''
O(n)
'''
def solution_while(phone_book):
    prefix_list = [{} for _ in range(20)]
    pn_list     = [{} for _ in range(20)]
    
    while phone_book:
        phone_num = phone_book.pop(0)
        num_len = len(phone_num)
        for n, (prefixes, pns) in enumerate(zip(prefix_list, pn_list), 1):
            if n >= num_len:
                break
            if prefixes.get(phone_num[:n]):
                return False
            pns[phone_num[:n]] = True
        if pn_list[num_len-1].get(phone_num):
            return False
        prefix_list[num_len-1][phone_num] = True
    return True

'''
O(n)
'''
def solution(phone_book):
    prefix_list = [{} for _ in range(20)]
    pn_list     = [{} for _ in range(20)]
    
    for phone_num in phone_book:
        num_len = len(phone_num)
        for n, (prefixes, pns) in enumerate(zip(prefix_list, pn_list), 1):
            if n >= num_len:
                break
            if prefixes.get(phone_num[:n]):
                return False
            pns[phone_num[:n]] = True
        if pn_list[num_len-1].get(phone_num):
            return False
        prefix_list[num_len-1][phone_num] = True
    return True