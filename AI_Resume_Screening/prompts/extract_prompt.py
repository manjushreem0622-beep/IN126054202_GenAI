from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate.from_template("""
You are an AI resume analyzer.

Read the resume carefully and extract only what is explicitly mentioned.

Resume:
{resume}

Return the output in this exact JSON format:
{{
  "skills": [],
  "tools": [],
  "experience": ""
}}

Rules:
- Do not assume missing skills
- Do not invent tools
- Keep experience short and factual
""")