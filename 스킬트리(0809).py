from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_order = deque(skill)
        for s in skill_tree:
            if s in skill:
                if s != skill_order.popleft():
                    break
        else:
            answer += 1

    return answer
