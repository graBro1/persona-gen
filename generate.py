from libs.genagents.genagents.genagents import GenerativeAgent
from libs.genagents.main import Conversation
from libs.genagents.simulation_engine.global_methods import *
from libs.genagents.simulation_engine.gpt_structure import *
from pathlib import Path
from datetime import datetime

class RichPersona:
  def __init__(self, scratch_path, demographics_path):
    self.agent = GenerativeAgent()
    self.social_circle = SocialCircle()
    self.scratch = read_json_to_dict(scratch_path)
    self.demographics = read_json_to_dict(demographics_path)
    self.name = f"{self.scratch["first_name"]} {self.scratch["last_name"]}"
    self.agent_folder = f"../libs/genagents/agent_bank/populations/single_agent/{self.agent.id}"
    self.interview_dialogue = None
    self.expert_insights = ""
    self.activities = None
    self.message_logs = []
    
    self.agent.update_scratch(self.scratch)
    self.agent.save(self.agent_folder)

  def interview(self, script):
    dict_script = read_json_to_dict(script)
    conversation = Conversation(self.agent_folder)

    self.interview_dialogue = conversation.start(dict_script)

  def create_insights(self, templates_path):
    templates_folder = Path(templates_path)
    for path in templates_folder.iterdir():
      prompt = generate_prompt([self.interview_dialogue], path)
      response = gpt_request(prompt, "gpt-4o-mini")
      self.expert_insights += f"{response}\n\n\n"

  def verify_insights(self, prompt_path):
    prompt = generate_prompt([self.name, str(self.scratch), self.interview_dialogue], prompt_path)
    verification_output = gpt_request(prompt, "gpt-4o-mini")
    return verification_output
  
  def create_social_circle(self, prompt_path):
    prompt = generate_prompt([self.expert_insights], prompt_path)
    response = gpt_request(prompt, "gpt-4o-mini")
    self.social_circle.social_circle_summary = json.loads(response)

  def create_circle_context(self, prompt_path):
    self.social_circle.generate_context(self.name, self.expert_insights, prompt_path)

  def create_activities(self, prompt_path):
    prompt = generate_prompt([self.scratch, self.expert_insights], prompt_path)
    response = gpt_request(prompt, "gpt-4o-mini")
    self.activities = json.loads(response)

  def create_filler_logs(self, prompt_path):
    for p in self.social_circle.persona_context[1:]:
      prompt = generate_prompt([self.demographics, p["name"], p["context"]], prompt_path)
      response = gpt_request(prompt, max_tokens=32000)
      self.message_logs.append({
        "participants": [
          {"name": p["name"]},
          {"name": self.name}
        ],
        "messages": json.loads(response)
      })

  def insert_needle_logs(self, prompt_path):
    for i, chat in enumerate(self.message_logs):
      prompt = generate_prompt([str(chat), self.name, self.social_circle.persona_context[0]["context"], self.activities, self.social_circle.persona_context[i+1]["name"], self.social_circle.persona_context[i+1]["context"]], prompt_path)
      response = gpt_request(prompt, max_tokens=32000)
      needles = json.loads(response)
      for conv in needles:
        dt_obj = datetime.fromisoformat(conv[0]["timestamp"])
        for j, v in enumerate(chat["messages"]):
          msg_dt = datetime.fromisoformat(v["timestamp"])
          if dt_obj < msg_dt:
            chat["messages"][j:j] = conv
            break    
    
class SocialCircle:
  def __init__(self):
    self.social_circle_summary = []
    self.persona_context = []

  def generate_context(self, character_name, character_insights, prompt_path):
    str_summary = str(self.social_circle_summary)
    prompt = generate_prompt([character_name, character_insights, str_summary], prompt_path)
    response = gpt_request(prompt, "gpt-4o-mini")
    self.persona_context = json.loads(response)

  



    
      
  
  