from .text_cleaner import clean_text
from .language import detect_language
from .normalizer import normalize_text
from .tokenizer import tokenize
from .classifier import classify_issue
from .urgency import urgency_score
from intelligence.models import Results


def start(report):
    text = report.message
    gps = report.gps
    
    clean_report = clean_text(text)
    language = detect_language(clean_report)
    if language != 'english':
        clean_report = normalize_text(clean_report, language)
    
    report_tokens = tokenize(clean_report)
    category = classify_issue(report_tokens)
    urgency = urgency_score(report_tokens)
    
    try:
        Results.objects.create(
            report=report,
            category=category,
            urgency=urgency,
            location=gps
        )
    except Exception:
        return False
    
    return True