higher_urgency = ["urgent","burst", "bursts", "bursted", "danger","emergency", "broken", "burst", "no", "without", "with out","help"]


def urgency_score(tokens):
    if any(word in tokens for word in higher_urgency):
        return "high"
    return "low"