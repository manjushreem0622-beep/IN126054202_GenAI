import json
from langchain_core.output_parsers import StrOutputParser
from prompts.explain_prompt import explain_prompt

def build_explain_chain(llm):
    parser = StrOutputParser()
    chain = explain_prompt | llm | parser

    def safe_json_load(result):
        try:
            result = result.strip()

            # 🔥 Remove ```json block
            if result.startswith("```"):
                result = result.replace("```json", "").replace("```", "").strip()

            return json.loads(result)

        except Exception as e:
            print("⚠️ Raw LLM Output (Explain):", result)
            return {}

    class ExplainWrapper:
        def invoke(self, inputs):
            result = chain.invoke(inputs)
            return safe_json_load(result)

    return ExplainWrapper()