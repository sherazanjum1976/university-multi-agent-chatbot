import os
from crewai import Agent, Task, Crew, Process, LLM

import admissions_agent
import fee_agent
import degree_agent
import general_agent

MODEL = "groq/openai/gpt-oss-120b"  # CrewAI/LiteLLM format: groq/<model>

SPECIALISTS = {
    "Admissions": admissions_agent,
    "Fee": fee_agent,
    "Degree & Programs": degree_agent,
    "General": general_agent,
}

KEYWORDS = {
    "Fee": ["fee", "tuition", "scholarship", "payment", "pay", "cost", "price", "refund", "installment", "discount", "waiver"],
    "Admissions": ["admission", "apply", "application", "deadline", "eligib", "document", "entrance", "test", "requirement", "intake"],
    "Degree & Programs": ["degree", "program", "course", "bs ", "ms ", "mba", "bba", "department", "faculty", "duration", "career", "major"],
}


def get_llm():
    """Create the Groq-backed CrewAI LLM using GROQ_API_KEY."""
    return LLM(
        model=MODEL,
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.2,
        max_tokens=2048,
    )


def keyword_route(query):
    """Simple fallback classifier used if the LLM classification fails."""
    q = query.lower()
    for label, words in KEYWORDS.items():
        if any(w in q for w in words):
            return label
    return "General"


def classify(query, llm):
    """Manager Agent decides which specialist should handle the query."""
    manager = Agent(
        role="University Chatbot Manager",
        goal="Route each student query to the correct specialist agent.",
        backstory="You are a manager who reads student questions and picks the right department.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    safe_query = query.replace("{", "(").replace("}", ")")
    task = Task(
        description=(
            "Classify the student query into exactly ONE category:\n"
            "- Admissions (requirements, eligibility, application process, deadlines, documents, entrance test)\n"
            "- Fee (tuition, admission fees, scholarships, payments, refunds)\n"
            "- Degree (degrees, programs, departments, duration, careers)\n"
            "- General (campus, hostels, transport, facilities, contact, anything else)\n\n"
            f"Student query: {safe_query}\n\n"
            "Reply with ONLY one word: Admissions, Fee, Degree, or General."
        ),
        expected_output="One word: Admissions, Fee, Degree, or General.",
        agent=manager,
    )
    crew = Crew(agents=[manager], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    text = (getattr(result, "raw", None) or str(result)).strip().lower()
    if "admission" in text:
        return "Admissions"
    if "fee" in text:
        return "Fee"
    if "degree" in text or "program" in text:
        return "Degree & Programs"
    if "general" in text:
        return "General"
    return keyword_route(query)


def handle_query(query, mode, llm, history, on_status):
    """Full workflow. on_status(message) is called at every stage. Returns (agent_name, answer)."""
    if mode == "Auto / Manager":
        on_status("🔍 Manager is analyzing your query...")
        try:
            label = classify(query, llm)
        except Exception:
            label = keyword_route(query)
            on_status("⚠️ Classifier unavailable, using keyword routing.")
        on_status(f"🧠 Query classified as: {label}")
    else:
        label = mode
        on_status(f"🧭 Manager: you selected {label}, skipping classification.")

    specialist = SPECIALISTS[label]
    on_status(f"🔄 Manager is handing the query to {specialist.NAME}...")
    on_status(f"{specialist.ICON} {specialist.NAME} is working on your query...")
    answer = specialist.run(query, llm, history)
    on_status(f"📥 Manager received the response from {specialist.NAME}.")
    on_status("✅ Manager is preparing the final response...")
    return f"{specialist.ICON} {specialist.NAME}", answer.strip()
