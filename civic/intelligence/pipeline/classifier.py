def classify_issue(tokens):
    scores = {
        "water":0,
        "roads":0,
        "bridge":0,
        "health":0,
        "garbage":0,
        "unknown":0
    }
    
    for token in tokens:
        if token == "water":
            scores["water"] += 3
            if tokens[tokens.index('water') - 1] == 'no':
                scores["water"] += 6
        elif token == "roads" or token == "road":
            scores["roads"] += 4
        elif token == "bridge":
            scores["bridge"] += 4
        elif token == "health":
            scores["health"] += 2
        elif token == "garbage":
            scores["garbage"] += 1
        else:
            continue
            
    max_score = max(scores.values())
    issue = ''
    for category in scores:
        if scores[category] == max_score:
            issue = category
    return issue