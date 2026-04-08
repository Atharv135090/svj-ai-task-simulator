from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, Tuple

class Observation(BaseModel):
    task_id: str
    task_type: str
    content: str
    correct_action: str

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    value: float

class SVJEnvironment:
    def __init__(self):
        self.action_space = ["spam", "not_spam", "clean", "ignore", "fix_bug", "no_issue"]
        self.tasks = [
            {
                "id": "email", 
                "type": "Email Classification", 
                "content": "Email: \"Win money now!!! Click here!\"\nObjective: Classify this email as spam or not_spam", 
                "correct_action": "spam"
            },
            {
                "id": "data", 
                "type": "Data Cleaning", 
                "content": "Input: Name = NULL\nObjective: Decide whether to clean or ignore the data", 
                "correct_action": "clean"
            },
            {
                "id": "code", 
                "type": "Code Review", 
                "content": "Code:\nprint(x)\nObjective: Identify whether the code contains a bug", 
                "correct_action": "fix_bug"
            }
        ]
        self.current_step = 0
        self.total_reward = 0
        self.streak = 0
        self.last_action_wrong = False
        self.done = False

    def reset(self) -> Observation:
        """ Resets the environment to its initial state. """
        self.current_step = 0
        self.total_reward = 0
        self.streak = 0
        self.last_action_wrong = False
        self.done = False
        return self.state()

    def state(self) -> Optional[Observation]:
        """ Returns the current observation / task. """
        if self.current_step >= len(self.tasks):
            return None
        task = self.tasks[self.current_step]
        return Observation(
            task_id=task["id"],
            task_type=task["type"],
            content=task["content"],
            correct_action=task["correct_action"]
        )

    def step(self, action: Action) -> Tuple[Optional[Observation], Reward, bool, dict]:
        """ Processes the action and returns (next_state, reward, done, info). """
        if self.done:
            return None, Reward(value=0.0), True, {"msg": "Episode already finished.", "correct": False}

        if action.action not in self.action_space:
            reward_val = -0.2
            self.streak = 0
            self.last_action_wrong = True
            info = {"msg": f"Invalid action! Allowed: {self.action_space}", "correct": False}
        else:
            current_task = self.tasks[self.current_step]
            correct_action = current_task["correct_action"]

            if action.action == correct_action:
                reward_val = 1.0
                self.streak += 1
                if self.streak > 1:
                    reward_val += 0.5  # Consecutive correct streak bonus
                self.last_action_wrong = False
                info = {"msg": "Correct action!", "correct": True}
            else:
                reward_val = -1.0
                self.streak = 0
                if self.last_action_wrong:
                    reward_val -= 1.0  # Repeated wrong action penalty
                self.last_action_wrong = True
                info = {"msg": f"Wrong action. Expected: {correct_action}", "correct": False}

        self.total_reward += reward_val
        self.current_step += 1
        
        if self.current_step >= len(self.tasks):
            self.done = True

        return self.state(), Reward(value=reward_val), self.done, info

    def close(self):
        """ Closes the environment. """
        pass
