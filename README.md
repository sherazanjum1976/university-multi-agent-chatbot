# 🎓 CUI Wah Campus Multi-Agent Chatbot

A chatbot for **COMSATS University Islamabad, Wah Campus** where a **Manager Agent** routes questions to
Admissions, Fee, Degree & Programs, or General specialist agents. Built with **CrewAI + Groq (`openai/gpt-oss-120b`) + Streamlit**.

## Knowledge base
All information lives in `university_data.py`, compiled from https://cuiwah.edu.pk. Items marked `[VERIFY]`
or "unofficial" come from third-party sources and should be checked. **Fees and dates change every semester.**
To update, edit the dictionaries in `university_data.py` and commit.

## Agents
| Agent | Responsibility |
|---|---|
| Manager | Classifies the query and delegates |
| Admissions | Eligibility, process, deadlines, documents |
| Fee | Fee structure, scholarships, payments |
| Degree & Programs | Departments, programs, eligibility |
| General | Campus, hostel, transport, facilities |

## Deploy (Streamlit Community Cloud)
1. Push this project to GitHub.
2. https://share.streamlit.io → Create app → branch `main`, main file `app.py`.
3. Advanced settings → Python 3.11, Secrets: `GROQ_API_KEY = "your_key_here"`
4. Deploy.

## Example queries
- What is the admission fee?
- What are the eligibility requirements for engineering?
- Is there a hostel and transport?
- Which departments does the Wah campus have?
