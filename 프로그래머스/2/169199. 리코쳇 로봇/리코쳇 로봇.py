
def get_next_pos(pos_cur, pos_list, side, limit=999):
    # side: 1 if go right else -1
    if side == 1:
        pos_list = [pid for pid in pos_list if pid > pos_cur]
    else:
        pos_list = [pid for pid in pos_list if pid < pos_cur]
    
    if pos_list:
        nearest_obs = min(pos_list, key=lambda x: side * (x - pos_cur))
        pos_next = nearest_obs - side
    else:
        pos_next = limit if side == 1 else 0
    
    if pos_next == pos_cur:
        return None
    else:
        return pos_next

def check_larger_side():
    pass

def solution(board):
    
    init_pos = None
    goal_pos = None
    obs_pos_row = [[] for _ in range(len(board))]
    obs_pos_col = [[] for _ in range(len(board[0]))]

    trail = [[] for _ in range(len(board))]
    
    for rid, row in enumerate(board):
        for cid, item in enumerate(list(row)):
            if item == "R":
                init_pos = (rid, cid)
            elif item == "G":
                goal_pos = (rid, cid)
            elif item == "D":
                obs_pos_row[rid].append(cid)
                obs_pos_col[cid].append(rid)
            trail[rid].append(False)

    queue = [init_pos, 0]
    answer = 0
    while queue:
        pos = queue.pop(0)
        
        # Termination Check
        if isinstance(pos, int):
            if queue:
                answer = pos + 1
                queue.append(answer)
                continue
            else:
                answer = -1
                break
        elif pos == goal_pos:
            break
        elif trail[pos[0]][pos[1]]:
            # print(f"Cycle : {pos}")
            continue
        else:
            trail[pos[0]][pos[1]] = True

        # Search
        rid, cid = pos
        for side in [1, -1]:
            next_cid = get_next_pos(cid, obs_pos_row[rid], side, limit=len(board[0])-1)
            next_rid = get_next_pos(rid, obs_pos_col[cid], side, limit=len(board)-1)
            if next_cid is not None:
                queue.append((rid, next_cid))
            if next_rid is not None:
                queue.append((next_rid, cid))
    
    # print(trail)
    
    return answer