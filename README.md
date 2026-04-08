# SVJ AI Task Simulator

## 📌 1. Project Overview
The SVJ AI Task Simulator is an advanced, visually appealing, and unique OpenEnv-compatible environment. It introduces real-world AI reasoning challenges natively within an interactive interface and CLI.
This is not a traditional grid-world simulation—it tests intelligence in practical software routines.

## 💡 2. Motivation
Most RL environments run simple physics games. The SVJ Simulator challenges autonomous models against real-world AI tasks:
- Processing and triaging emails
- Cleaning massive raw datasets
- Catching bugs in production logic

## 📋 3. Task Explanation
1. 📧 Email Intelligence (Easy): Classify text messages. E.g., "Win money now!!!" -> spam.
2. 🧹 Smart Data Cleaning (Medium): React to incomplete or NaN data natively. Action: "clean" vs "ignore".
3. 💻 AI Code Reviewer (Hard): Analyze strict Python logic for obvious bugs. E.g., subtraction instead of addition.

## 🎮 4. Action & Observation Space
- Action Space: `["spam", "not_spam", "clean", "ignore", "fix_bug", "no_issue"]`
- Observation Space: Typed Pydantic object `SVJObservation` with structured state tracking (e.g., task_id, task_type, content).

## 💰 5. Reward Logic
We incorporated a highly balanced risk-reward architecture:
- +1.0: Correct action
- -1.0: Wrong action
- -0.2: Invalid action
- +0.5: Consecutive correct streak bonus
- -1.0: Repeated wrong action penalty

## 🚀 6. Project Structure

For full OpenEnv validation compliance, the project follows this structure:

```text
ROOT/
├── openenv.yaml
├── inference.py
├── Dockerfile
├── README.md
├── requirements.txt
├── envs/
│   └── svj_ai_simulator/
│       ├── main.py
│       ├── grader.py
│       ├── __init__.py
│       └── frontend/
│           ├── index.html
│           ├── style.css
│           └── script.js
```

## 🚀 7. How to Run

### OpenEnv Evaluation Script
The environment ships with `inference.py`, which is strictly compatible with the OpenEnv evaluation standards.

1. Ensure Python 3.10+ is installed.
2. Install requirements:
   `pip install -r requirements.txt`
3. Run the reference script:
   `python inference.py`

### Docker Support
`docker build -t svj-ai-task-simulator .`
`docker run --rm svj-ai-task-simulator`

## 🎨 8. Baseline Performance
Baseline scores running against GPT-4o-mini:
- Email Intelligence: 100%
- Smart Data Cleaning: 100%
- AI Code Reviewer: 100%
- Overall Score: 1.0 (100%)
