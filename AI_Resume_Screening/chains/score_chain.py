import json
from langchain_core.output_parsers import StrOutputParser
from prompts.score_prompt import score_prompt

def build_score_chain(llm):
    parser = StrOutputParser()
    chain = score_prompt | llm | parser

    def safe_json_load(result):
        try:
            result = result.strip()

            # 🔥 Remove ```json block
            if result.startswith("```"):
                result = result.replace("```json", "").replace("```", "").strip()

            return json.loads(result)

        except Exception as e:
            print("⚠️ Raw LLM Output (Score):", result)
            return {}

    class ScoreWrapper:
        def invoke(self, inputs):
            result = chain.invoke(inputs)
            return safe_json_load(result)

    return ScoreWrapper()