def answer_iterator(template):
    i = 0
    while True:
        yield template[i]
        i = (i + 1) % len(template)

def solution(answers):
    player1 = answer_iterator([1,2,3,4,5])
    player2 = answer_iterator([2,1,2,3,2,4,2,5])
    player3 = answer_iterator([3,3,1,1,2,2,4,4,5,5])
    
    scores = [0, 0, 0]
    for i, (ans1, ans2, ans3) in enumerate(zip(player1, player2, player3)):
        if i >= len(answers):
            break
        answer = answers[i]
        if ans1 == answer:
            scores[0] += 1
        if ans2 == answer:
            scores[1] += 1
        if ans3 == answer:
            scores[2] += 1
    
    max_score = 0
    max_players = []
    for i, score in enumerate(scores):
        if score > max_score:
            max_players = [i+1]
            max_score = score
        elif score == max_score:
            max_players.append(i+1)
        else:
            pass
    return max_players