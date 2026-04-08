import os
import sys
from envs.svj_ai_task_simulator.grader import grade_email, grade_data, grade_code
from envs.svj_ai_task_simulator.main import SVJEnvironment, Action

MODEL_NAME = os.getenv("MODEL_NAME", "rule-based")

def run_inference():
    env = SVJEnvironment()
    state = env.reset()
    
    history = []
    episode_rewards = []
    
    print(f"[START] task=svj env=svj model={MODEL_NAME}", flush=True)

    is_done = False
    try:
        while not is_done:
            step = env.current_step + 1

            if step == 1:
                action_str = "spam"
            elif step == 2:
                action_str = "clean"
            elif step == 3:
                action_str = "fix_bug"
            else:
                action_str = "not_spam"

            action_obj = Action(action=action_str)

            next_state, reward_obj, done_flag, info = env.step(action_obj)

            reward_val = reward_obj.value
            episode_rewards.append(reward_val)

            history.append({
                "task_id": state.task_id if state else "unknown",
                "correct": info.get("correct", False)
            })

            print(f"[STEP] step={env.current_step} action={action_str} reward={reward_val:.2f} done={str(done_flag).lower()}", flush=True)

            state = next_state
            is_done = done_flag

        env.close()

        e_score = grade_email(history)
        d_score = grade_data(history)
        c_score = grade_code(history)
        is_success = (e_score >= 0.5 and d_score >= 0.5 and c_score >= 0.5)

        rewards_str = ",".join([f"{r:.2f}" for r in episode_rewards])
        print(f"[END] success={str(is_success).lower()} steps={env.current_step} rewards={rewards_str}", flush=True)

    except Exception as e:
        env.close()
        print(f"[END] success=false steps={env.current_step} rewards=", flush=True)
        raise e

if __name__ == "__main__":
    run_inference()
