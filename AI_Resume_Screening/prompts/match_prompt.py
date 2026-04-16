from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate.from_template("""
You are comparing a resume with a job description.

Job Description:
{job_description}

Resume Data:
{resume_data}

Return ONLY valid JSON:

{{
  "matched_skills": [],
  "missing_skills": [],
  "match_percentage": 0
}}

Rules:
- match_percentage must be between 0–100
- Do NOT return text outside JSON
""")