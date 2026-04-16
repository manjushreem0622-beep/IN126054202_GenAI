import os
import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langsmith import traceable

from chains.extract_chain import build_extract_chain
from chains.match_chain import build_match_chain
from chains.score_chain import build_score_chain
from chains.explain_chain import build_explain_chain

load_dotenv()

import os
print("GROQ:", os.getenv("GROQ_API_KEY"))
print("LANGSMITH:", os.getenv("LANGCHAIN_API_KEY"))


def check_environment():
    required_vars = ["GROQ_API_KEY"]
    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {missing}\n"
            "Please add them to your .env file."
        )

    if os.getenv("LANGCHAIN_TRACING_V2") == "true":
        if os.getenv("LANGCHAIN_API_KEY"):
            print("LangSmith tracing is enabled.")
            print(f"Project: {os.getenv('LANGCHAIN_PROJECT', 'ai-resume-screening')}")
        else:
            print("Warning: LANGCHAIN_TRACING_V2 is true but LANGCHAIN_API_KEY is missing.")


def build_llm():
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=1024
    )


@traceable(name="resume_screening_pipeline")
def screen_resume(resume_text, job_description, candidate_name="Candidate"):
    llm = build_llm()

    extract_chain = build_extract_chain(llm)
    match_chain = build_match_chain(llm)
    score_chain = build_score_chain(llm)
    explain_chain = build_explain_chain(llm)

    print("\n" + "=" * 60)
    print(f"Screening: {candidate_name}")
    print("=" * 60)

    print("\nStep 1: Extracting resume details...")
    extracted_data = extract_chain.invoke({"resume": resume_text})
    print(json.dumps(extracted_data, indent=2))

    print("\nStep 2: Matching with job description...")
    match_result = match_chain.invoke({
        "resume_data": json.dumps(extracted_data),
        "job_description": job_description
    })
    print(json.dumps(match_result, indent=2))

    print("\nStep 3: Calculating score...")
    score_result = score_chain.invoke({
        "match_result": json.dumps(match_result)
    })
    print(json.dumps(score_result, indent=2))

    print("\nStep 4: Generating explanation...")
    explain_result = explain_chain.invoke({
        "resume_data": json.dumps(extracted_data),
        "match_result": json.dumps(match_result),
        "score": score_result["score"]
    })
    print(json.dumps(explain_result, indent=2))

    final_output = {
        "candidate": candidate_name,
        "score": score_result["score"],
        "explanation": explain_result["explanation"]
    }

    print("\nFinal Result:")
    print(json.dumps(final_output, indent=2))

    return final_output


def run_demo():
    data_folder = Path("data")

    job_description = (data_folder / "job_description.txt").read_text(encoding="utf-8")

    resumes = [
        ("Strong Candidate", data_folder / "strong_resume.txt"),
        ("Average Candidate", data_folder / "average_resume.txt"),
        ("Weak Candidate", data_folder / "weak_resume.txt"),
    ]

    all_results = {}

    for candidate_name, file_path in resumes:
        resume_text = file_path.read_text(encoding="utf-8")
        try:
            result = screen_resume(resume_text, job_description, candidate_name)
            all_results[candidate_name] = result
        except Exception as e:
            print(f"Error while processing {candidate_name}: {e}")
            all_results[candidate_name] = {"error": str(e)}    
    print("\n" + "=" * 60)
    print("DEBUG TEST CASE")
    print("=" * 60)

    debug_resume = "Python, no ML, no experience"
    debug_result = screen_resume(debug_resume, job_description, "Debug Candidate")

    print("\nDebug Result:")
    print(debug_result) 
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)


    for name, result in all_results.items():
        if "score" in result:
            print(f"{name}: {result['score']}/100")
        else:
            print(f"{name}: ERROR")

    return all_results


if __name__ == "__main__":
    check_environment()
    run_demo()



