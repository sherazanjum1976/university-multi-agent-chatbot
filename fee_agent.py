from crewai import Agent, Task, Crew, Process
from university_data import FEES, build_prompt

NAME = "Fee Agent"
ICON = "💰"


def run(query, llm, history=""):
    agent = Agent(
        role="University Fee and Scholarship Advisor",
        goal="Answer questions about tuition, admission fees, scholarships and payment options.",
        backstory="You work in the accounts office and explain fees and financial aid clearly.",
        llm=llm,
        allow_delegation=False,
        verbose=False,
    )
    task = Task(
        description=build_prompt("Fees and Scholarships", FEES, query, history),
        expected_output="A short, friendly and accurate answer for the student.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    result = crew.kickoff()
    return getattr(result, "raw", None) or str(result)
