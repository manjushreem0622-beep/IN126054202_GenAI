import json
from langchain_core.output_parsers import StrOutputParser
from prompts.match_prompt import match_prompt

def build_match_chain(llm):
    parser = StrOutputParser()
    chain = match_prompt | llm | parser

    def safe_json_load(result):
        try:
            result = result.strip()

            # 🔥 Remove ```json block
            if result.startswith("```"):
                result = result.replace("```json", "").replace("```", "").strip()

            return json.loads(result)

        except Exception as e:
            print("⚠️ Raw LLM Output (Match):", result)
            return {}

    class MatchWrapper:
        def invoke(self, inputs):
            result = chain.invoke(inputs)
            return safe_json_load(result)

    return MatchWrapper()