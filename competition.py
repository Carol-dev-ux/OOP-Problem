def sort_key(score):
    return (-score['score'], score['name'])

def calculate_score(participants):
    scores = []

    for participant in participants:
        score = participant['chickenwings'] * 5 + participant['hamburgers'] * 3 + participant['hotdogs'] * 2
        scores.append({'name': participant['name'], 'score': score})

    scores.sort(key=sort_key)
    
    return scores

# Example 
participants = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = calculate_score(participants)
print(scoreboard)

