def grade_email(history):
    email_tasks = [h for h in history if h['task_id'] == "email"]
    if not email_tasks: return 0.0
    correct = sum(1 for h in email_tasks if h['correct'])
    return correct / len(email_tasks)
    
def grade_data(history):
    data_tasks = [h for h in history if h['task_id'] == "data"]
    if not data_tasks: return 0.0
    correct = sum(1 for h in data_tasks if h['correct'])
    return correct / len(data_tasks)

def grade_code(history):
    code_tasks = [h for h in history if h['task_id'] == "code"]
    if not code_tasks: return 0.0
    correct = sum(1 for h in code_tasks if h['correct'])
    return correct / len(code_tasks)
