def resolveUserPresense(user1, user2):
    if len(user1) == 0 or len(user2) == 0:
        return []
    user1_index = 0
    user2_index = 0
    users_online = 0
    result = []
    while user1_index < len(user1) and user2_index < len(user2):
        start_session = max(user1[user1_index][0], user2[user2_index][0])
        # end_session = min(user1[user1_index][1], user2[user2_index][1])
        if user1[user1_index][1] < user2[user2_index][1]:
            end_session = user1[user1_index][1]
            user1_index += 1
        else:
            end_session = user2[user2_index][1]
            user2_index += 1
        if end_session > start_session:
            session = (start_session, end_session)
            result.append(session)
        else:
            pass # сессии не случилось
    return result

user1 = [(10, 12), (17, 22)]
user2 = [(8, 11), (14, 18), (20, 23)]
print(resolveUserPresense(user1, user2))