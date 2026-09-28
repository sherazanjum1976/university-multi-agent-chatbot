# 🎓 Multi-Agent University Chatbot (Demo MVP)

A beginner-friendly chatbot where a **Manager Agent** routes student questions to specialist agents.
Built with **CrewAI + Groq (`openai/gpt-oss-120b`) + Streamlit**.

> All university data is **fictional demo data** (`university_data.py`). Replace it with real information later.

## Features
- Manager → specialist delegation (Auto mode) or manual agent selection
- Visible workflow status for every request
- Modern, high-contrast chat UI with a clear-chat button
- Session chat history, graceful error handling, missing-key detection
- No PDFs, database, RAG or scraping required

## Architecture
User → Streamlit (`app.py`) → Manager (`manager_agent.py`) → Specialist Agent → Manager → User

## Agents
| Agent | Responsibility |
|---|---|
| Manager | Classifies the query and delegates |
| Admissions | Eligibility, process, deadlines, documents |
| Fee | Tuition, scholarships, payments, refunds |
| Degree & Programs | Programs, duration, eligibility, careers |
| General | Campus, hostels, transport, contacts |

## Project structure
```
app.py, manager_agent.py, admissions_agent.py, fee_agent.py,
degree_agent.py, general_agent.py, university_data.py,
requirements.txt, README.md, .gitignore, .streamlit/config.toml
```

## Groq API key
Create a free key at https://console.groq.com/keys.

## Deploy (Streamlit Community Cloud)
1. Push this project to a GitHub repository.
2. Go to https://share.streamlit.io → **Create app** → pick the repo, branch `main`, main file `app.py`.
3. Advanced settings → **Python 3.11**, and paste in Secrets: `GROQ_API_KEY = "your_key_here"`
4. Click **Deploy**.

## Example queries
- What are the admission requirements for undergraduate programs?
- How much is the tuition for Computer Science?
- Which scholarships are available?
- How long is the MBA and what careers does it lead to?
- Is there a hostel on campus?

## Future ideas
- Replace demo data with real university content
- Add RAG over PDFs, then a vector database
- Stream answers token by token
- Add a final Manager review step, feedback buttons and chat export
