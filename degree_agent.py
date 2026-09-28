from crewai import Agent, Task, Crew, Process
from university_data import PROGRAMS, build_prompt

NAME = "Degree & Programs Agent"
ICON = "📚"


def run(query, llm, history=""):
    agent = Agent(
        role="Academic Programs Counselor",
        goal="Answer questions about degrees, programs, departments, duration, eligibility and careers.",
        backstory="You are an academic counselor who helps students choose the right program.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    task = Task(
        description=build_prompt("Degrees and Programs", PROGRAMS, query, history),
        expected_output="A short, friendly and accurate answer for the student.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return getattr(result, "raw", None) or str(result)
