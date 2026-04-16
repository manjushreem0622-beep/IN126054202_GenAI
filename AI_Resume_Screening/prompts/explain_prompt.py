from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate.from_template("""
Explain the candidate evaluation.

Resume Data:
{resume_data}

Match Result:
{match_result}

Score:
{score}

Return ONLY JSON:

{{
  "explanation": [
    "",
    "",
    ""
  ]
}}

Rules:
- Give 3–4 points
- No extra text
""")