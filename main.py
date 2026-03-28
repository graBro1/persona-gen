from generate import RichPersona
from libs.genagents.simulation_engine.global_methods import *

# Example:

def main():
    persona = RichPersona("data/step_1/mary_alberti.json", "data/step_1/mary_alberti_demographics.json")

    # Initiate Interview
    persona.interview("data/step_2/input/script.json")
    write_string_to_file("data/step_2/interview_dialogue.txt", persona.interview_dialogue)

    # Expert reflection of interview dialogue
    persona.create_insights("data/step_2/input/expert_templates")
    print(persona.expert_insights)
    write_string_to_file("data/step_2/expert_insights.txt", persona.expert_insights)

    # Verify consistency between original profile and interview responses
    print(persona.verify_insights("data/step_2/input/verification_prompt.txt"))

    # Initialize social circle
    persona.create_social_circle("data/step_3/input/init_circle_prompt.txt")
    print(persona.social_circle.social_circle_summary)
    write_dict_to_json(persona.social_circle.social_circle_summary, "data/step_3/social_circle_summary.json")

    # Create hidden context for social circle
    persona.create_circle_context("data/step_3/input/circle_context_prompt.txt")
    print(persona.social_circle.persona_context)
    write_dict_to_json(persona.social_circle.persona_context, "data/step_3/social_circle_context.json")

    # Create calendar/activity logs for main persona (step 4 + 5)
    persona.create_activities("data/step_4_5/input/create_activities_prompt.txt")
    print(persona.activities)
    write_dict_to_json(persona.activities, "data/step_4_5/calendar.json")

    # Create filler messages (long context) between main persona and their social circle
    persona.create_filler_logs("data/step_4_5/input/filler_messages_prompt.txt")
    print("Filler messages:")
    print(persona.message_logs)
    write_dict_to_json(persona.message_logs, "data/step_4_5/filler_messages.json")

    # Create and insert messages influenced by context
    persona.insert_needle_logs("data/step_4_5/input/needle_messages_prompt.txt")
    print("Messages with context:")
    print(persona.message_logs)
    write_dict_to_json(persona.message_logs, "data/step_4_5/message_logs.json")

if __name__ == "__main__":
    main()