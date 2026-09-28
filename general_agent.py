from crewai import Agent, Task, Crew, Process
from university_data import GENERAL, build_prompt

NAME = "General Agent"
ICON = "🏛️"


def run(query, llm, history=""):
    agent = Agent(
        role="University Information Desk Assistant",
        goal="Answer general questions about the campus, facilities, hostels, transport and contacts.",
        backstory="You staff the university information desk and know the campus inside out.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    task = Task(
        description=build_prompt("General campus information", GENERAL, query, history),
        expected_output="A short, friendly and accurate answer for the student.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return getattr(result, "raw", None) or str(result)
