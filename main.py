from tools import list_topics, estimate_effort, calculate

MAX_STEPS = 8


def run_agent(goal):
    print("Goal:", goal)

    steps = 0

    topics = []
    study_plan = []

    while steps < MAX_STEPS:
        steps += 1

        if steps == 1:
            topics = list_topics()
            print("\nSTEP 1: TOOL -> list_topics()")
            print("RESULT:", topics)

        elif 2 <= steps <= len(topics) + 1:
            topic = topics[steps - 2]["name"]

            result = estimate_effort(topic)

            study_plan.append(result)

            print(f"\nSTEP {steps}: TOOL -> estimate_effort({topic})")
            print("RESULT:", result)

        elif steps == len(topics) + 2:
            total_expression = "+".join(
                [str(item["hours"]) for item in study_plan]
            )

            total = calculate(total_expression)

            print(f"\nSTEP {steps}: TOOL -> calculate({total_expression})")
            print("RESULT:", total)

            final_output = {
                "study_plan": study_plan,
                "total_hours": total["result"]
            }

            print("\nFINAL OUTPUT:")
            print(final_output)
            break


goal = "Build me a study plan for my exam with total hours."

run_agent(goal)