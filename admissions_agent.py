from crewai import Agent, Task, Crew, Process
from university_data import ADMISSIONS, build_prompt

NAME = "Admissions Agent"
ICON = "🎓"


def run(query, llm, history=""):
    agent = Agent(
        role="University Admissions Advisor",
        goal="Answer questions about admission requirements, eligibility, process, deadlines and documents.",
        backstory="You are a helpful admissions officer who knows the application process well.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    task = Task(
        description=build_prompt("Admissions", ADMISSIONS, query, history),
        expected_output="A short, friendly and accurate answer for the student.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return getattr(result, "raw", None) or str(result)
