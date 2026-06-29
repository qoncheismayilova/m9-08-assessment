![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Assessment | Ship a Multi-Tool Agent

## Overview

This project is a **Study Planner Agent** built using a hand-rolled agent loop in Python.

The agent uses three tools to solve a multi-step goal:

> Build me a study plan for my exam with total hours.

The agent decides which tools to use step by step, calculates the effort for each topic, and returns a structured result.

---

## Scenario

I chose the **Study Planner** scenario.

This scenario is useful because exam preparation requires:
- identifying topics
- estimating study time for each topic
- calculating total study hours

A single tool cannot complete this task alone.

---

## Tools Used

### 1. `list_topics()`

Returns all exam topics from `topics.json`.

Example:

```python
list_topics()
```

---

### 2. `estimate_effort(topic)`

Estimates study hours for a topic based on its difficulty.

Example:

```python
estimate_effort("Machine Learning")
```

Returns:

```json
{
  "topic": "Machine Learning",
  "hours": 6
}
```

---

### 3. `calculate(expression)`

Calculates the total study hours.

Example:

```python
calculate("4+2+6+6+2")
```

Returns:

```json
{
  "result": 20
}
```

---

## Why These Tools?

These three tools work together:

- `list_topics()` retrieves the exam topics
- `estimate_effort()` assigns study hours to each topic
- `calculate()` sums all study hours

This creates a complete study plan.

---

## Reliability

The agent uses a **step limit**:

```python
MAX_STEPS = 8
```

This prevents infinite loops and ensures the program stops safely.

If the goal cannot be completed, the agent will stop after the maximum number of steps.

This protects the system from running forever.

---

## Safety

The `calculate()` tool validates input before executing.

Only numbers and mathematical operators are allowed:

```python
allowed = "0123456789+-*/(). "
```

This protects against code injection attacks such as:

```python
__import__("os").system("rm -rf /")
```

Without validation, malicious code could execute.

This mitigation ensures tool inputs are treated as untrusted.

---

## Project Structure

```text
m9-08-assessment/
│── main.py
│── tools.py
│── topics.json
│── README.md
│── .gitignore
```

---

## Example Run

Goal:

```text
Build me a study plan for my exam with total hours.
```

Execution:

```text
Goal: Build me a study plan for my exam with total hours.

STEP 1: TOOL -> list_topics()
RESULT: [{'id': 'topic-1', 'name': 'Linear Algebra', 'difficulty': 'medium'}, {'id': 'topic-2', 'name': 'Python Basics', 'difficulty': 'easy'}, {'id': 'topic-3', 'name': 'Machine Learning', 'difficulty': 'hard'}, {'id': 'topic-4', 'name': 'Statistics', 'difficulty': 'hard'}, {'id': 'topic-5', 'name': 'Data Visualization', 'difficulty': 'easy'}]

STEP 2: TOOL -> estimate_effort(Linear Algebra)
RESULT: {'topic': 'Linear Algebra', 'hours': 4}

STEP 3: TOOL -> estimate_effort(Python Basics)
RESULT: {'topic': 'Python Basics', 'hours': 2}

STEP 4: TOOL -> estimate_effort(Machine Learning)
RESULT: {'topic': 'Machine Learning', 'hours': 6}

STEP 5: TOOL -> estimate_effort(Statistics)
RESULT: {'topic': 'Statistics', 'hours': 6}

STEP 6: TOOL -> estimate_effort(Data Visualization)
RESULT: {'topic': 'Data Visualization', 'hours': 2}

STEP 7: TOOL -> calculate(4+2+6+6+2)
RESULT: {'result': 20}

FINAL OUTPUT:
{'study_plan': [{'topic': 'Linear Algebra', 'hours': 4}, {'topic': 'Python Basics', 'hours': 2}, {'topic': 'Machine Learning', 'hours': 6}, {'topic': 'Statistics', 'hours': 6}, {'topic': 'Data Visualization', 'hours': 2}], 'total_hours': 20}
```

---

## Final Structured Output

```json
{
  "study_plan": [
    {
      "topic": "Linear Algebra",
      "hours": 4
    },
    {
      "topic": "Python Basics",
      "hours": 2
    },
    {
      "topic": "Machine Learning",
      "hours": 6
    },
    {
      "topic": "Statistics",
      "hours": 6
    },
    {
      "topic": "Data Visualization",
      "hours": 2
    }
  ],
  "total_hours": 20
}
```

---

## How to Run

Install dependencies:

```bash
pip install python-dotenv
```

Run the project:

```bash
python main.py
```

---

## Notes

- This project uses a **hand-rolled agent loop** instead of Google ADK.
- The agent performs **multi-step reasoning** by calling three tools.
- The output is **structured and parseable**.
- The system includes **reliability protection** (step limit).
- The system includes **safety protection** (input validation).