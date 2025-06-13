def create_prompt(goal, duration, level):
    return f"""
    You are an expert AI tutor. Create a detailed {duration} study plan for someone at {level} level who wants to {goal}.
    Break it into weekly or daily tasks with clear objectives and action items.
    
