higher_urgency = ["urgent","burst","danger","emergency", "broken","no", "without", "with out","help"]


def urgency_score(tokens):
    if any(word in tokens for word in higher_urgency):
        return "high"
    return "low"