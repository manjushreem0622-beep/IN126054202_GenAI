import json
from langchain_core.output_parsers import StrOutputParser
from prompts.extract_prompt import extract_prompt

def build_extract_chain(llm):
    parser = StrOutputParser()
    chain = extract_prompt | llm | parser

    def safe_json_load(result):
        try:
            result = result.strip()

            # 🔥 Remove ```json code block if present
            if result.startswith("```"):
                result = result.replace("```json", "").replace("```", "").strip()

            return json.loads(result)

        except Exception as e:
            print("⚠️ Raw LLM Output (Extract):", result)
            return {}

    class ExtractWrapper:
        def invoke(self, inputs):
            result = chain.invoke(inputs)
            return safe_json_load(result)

    return ExtractWrapper()