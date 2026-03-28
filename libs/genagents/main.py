from simulation_engine.global_methods import *
from genagents.genagents import GenerativeAgent

class Conversation:
  def __init__(self, agent_folder, interviewer_name="Interviewer"):
    # Load the agent from the specified folder
    self.agent = GenerativeAgent(agent_folder)
    self.interviewer_name = interviewer_name
    self.conversation_history = []
    self.str_dialogue = ""
      
  def start(self, script):
    print(f"Starting conversation with {self.agent.get_fullname()}.\n")
    for interview_question in script:
      print(f"{self.interviewer_name}: {interview_question}")
      # Add the interviewer's utterance to the conversation history
      self.str_dialogue += f"{self.interviewer_name}: {interview_question}\n"
      self.conversation_history.append([self.interviewer_name, interview_question])
      # Get the agent's response
      agent_response = self.agent.utterance(self.conversation_history)
      print(f"{self.agent.get_fullname()}: {agent_response}")
      # Add the agent's response to the conversation history
      self.str_dialogue += f"{self.agent.get_fullname()}: {agent_response}\n"
      self.conversation_history.append([self.agent.get_fullname(), agent_response])
    
    print("Conversation ended.")
    return self.str_dialogue

# Example usage:
if __name__ == "__main__":
  # Specify the folder where the agent is stored
  agent_folder = "agent_bank/populations/single_agent/01fd7d2a-0357-4c1b-9f3e-8eade2d537ae"
  # Create a Conversation instance
  conversation = Conversation(agent_folder, interviewer_name="Jane Doe")
  # Start the conversation
  conversation.start()
