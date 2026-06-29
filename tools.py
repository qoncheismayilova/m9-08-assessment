import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOPICS_PATH = os.path.join(BASE_DIR, "topics.json")

with open(TOPICS_PATH, "r") as f:
    topics = json.load(f)


def list_topics():
    return topics


def estimate_effort(topic_name):
    for topic in topics:
        if topic["name"] == topic_name:
            difficulty = topic["difficulty"]

            if difficulty == "easy":
                return {"topic": topic_name, "hours": 2}
            elif difficulty == "medium":
                return {"topic": topic_name, "hours": 4}
            elif difficulty == "hard":
                return {"topic": topic_name, "hours": 6}

    return {"error": "Topic not found"}


def calculate(expression):
    allowed = "0123456789+-*/(). "

    # safety mitigation
    if not all(char in allowed for char in expression):
        return {"error": "Unsafe input"}

    try:
        return {"result": eval(expression)}
    except Exception:
        return {"error": "Calculation failed"}