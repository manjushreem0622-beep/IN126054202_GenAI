from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate.from_template("""
Assign a final score.

Match Result:
{match_result}

Consider:
- Match percentage
- Missing critical skills
- Experience level

Return ONLY JSON:

{{
  "score": 0
}}

Rules:
- Score must be 0–100
- Penalize missing important skills
- Reward experience
""")