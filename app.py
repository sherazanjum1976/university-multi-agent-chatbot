# --- Streamlit Cloud sqlite fix (CrewAI/chromadb needs newer sqlite) ---
try:
    __import__("pysqlite3")
    import sys
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except Exception:
    pass

import os
os.environ["CREWAI_DISABLE_TELEMETRY"] = "true"
os.environ["OTEL_SDK_DISABLED"] = "true"

import streamlit as st

st.set_page_config(page_title="Northbridge University Assistant", page_icon="🎓", layout="wide")

from manager_agent import get_llm, handle_query
from university_data import UNIVERSITY_NAME

MODES = ["Auto / Manager", "Admissions", "Fee", "Degree & Programs", "General"]

st.markdown(
    """
<style>
.hero {background: linear-gradient(135deg,#0B1F4B 0%,#1D4ED8 100%); padding: 26px 30px;
       border-radius: 18px; border-bottom: 5px solid #F5B301; margin-bottom: 18px;}
.hero h1 {color:#FFFFFF !important; margin:0; font-size: 2rem;}
.hero p {color:#E0E7FF; margin:6px 0 0 0; font-size: 1rem;}
.badge {display:inline-block; background:#F5B301; color:#0B1F4B; font-weight:700;
        padding:2px 10px; border-radius:20px; font-size:0.75rem; margin-top:10px;}
[data-testid="stChatMessage"] {border:1px solid #CBD5E1; border-radius:14px; padding:12px 16px;
        background:#FFFFFF; margin-bottom:10px; box-shadow:0 1px 3px rgba(15,23,42,.08);}
.agent-tag {display:inline-block; background:#0B1F4B; color:#FFFFFF; padding:2px 10px;
        border-radius:12px; font-size:0.78rem; font-weight:600; margin-bottom:6px;}
[data-testid="stSidebar"] {background:#EEF2FF; border-right:2px solid #1D4ED8;}
@media (max-width: 640px) {.hero h1 {font-size:1.4rem;} .hero {padding:18px;}}
</style>
<div class="hero">
  <h1>🎓 Northbridge University Assistant</h1>
  <p>Multi-agent chatbot: a Manager routes your question to the right specialist.</p>
  <span class="badge">DEMO • Fictional university data</span>
</div>
""",
    unsafe_allow_html=True,
)


def get_api_key():
    key = os.environ.get("GROQ_API_KEY")
    if not key:
        try:
            key = st.secrets["GROQ_API_KEY"]
        except Exception:
            key = None
    if key:
        os.environ["GROQ_API_KEY"] = key
    return key


def friendly_error(exc):
    text = str(exc).lower()
    if "401" in text or "invalid api key" in text or "authentication" in text:
        return "Your Groq API key looks invalid. Please check the GROQ_API_KEY secret."
    if "429" in text or "rate limit" in text:
        return "Groq rate limit reached. Please wait a moment and try again."
    if "connection" in text or "timeout" in text:
        return "Could not reach Groq. Please try again shortly."
    return f"Something went wrong ({type(exc).__name__}). Please try again."


def build_history(messages, limit=6):
    lines = []
    for m in messages[-limit:]:
        who = "Student" if m["role"] == "user" else "Assistant"
        lines.append(f"{who}: {m['content']}")
    return "\n".join(lines)


api_key = get_api_key()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    mode = st.radio("Query type", MODES, help="Auto lets the Manager pick the specialist.")
    if api_key:
        st.success("🔑 GROQ_API_KEY: found")
    else:
        st.error("🔑 GROQ_API_KEY: missing")
        st.caption("Add it in Streamlit Cloud → App settings → Secrets.")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown("### 🤖 Agents")
    st.markdown(
        "- 🧑‍💼 **Manager**: analyzes & delegates\n"
        "- 🎓 **Admissions**: requirements, deadlines, documents\n"
        "- 💰 **Fee**: tuition, scholarships, payments\n"
        "- 📚 **Degree & Programs**: degrees, duration, careers\n"
        "- 🏛️ **General**: campus, hostels, contacts"
    )
    st.caption(f"Data source: {UNIVERSITY_NAME} sample data.")

# ---------------- Chat history ----------------
if not st.session_state.messages:
    st.info("👋 Ask me about admissions, fees, programs or campus life. Try: *What scholarships are available?*")

for m in st.session_state.messages:
    avatar = "🧑‍🎓" if m["role"] == "user" else "🎓"
    with st.chat_message(m["role"], avatar=avatar):
        if m["role"] == "assistant":
            st.markdown(f"<span class='agent-tag'>Handled by {m['agent']}</span>", unsafe_allow_html=True)
        st.markdown(m["content"])
        if m.get("workflow"):
            with st.expander("Workflow steps"):
                for step in m["workflow"]:
                    st.write(step)

# ---------------- New message ----------------
if not api_key:
    st.warning("Add GROQ_API_KEY to enable the chatbot.")

prompt = st.chat_input("Ask a question about the university...", disabled=not api_key)

if prompt is not None:
    prompt = prompt.strip()
    if not prompt:
        st.warning("Please type a question first.")
    elif len(prompt) > 1000:
        st.warning("Please keep your question under 1000 characters.")
    else:
        with st.chat_message("user", avatar="🧑‍🎓"):
            st.markdown(prompt)
        history_text = build_history(st.session_state.messages)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant", avatar="🎓"):
            steps = []
            status = st.status("🔍 Starting workflow...", expanded=True)

            def on_status(msg):
                steps.append(msg)
                status.write(msg)
                status.update(label=msg, state="running")

            try:
                llm = get_llm()
                agent_name, answer = handle_query(prompt, mode, llm, history_text, on_status)
                steps.append("💬 Returning the answer to the user.")
                status.write(steps[-1])
                status.update(label="Done", state="complete", expanded=False)
                st.markdown(f"<span class='agent-tag'>Handled by {agent_name}</span>", unsafe_allow_html=True)
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer, "agent": agent_name, "workflow": steps}
                )
            except Exception as exc:
                status.update(label="Error", state="error", expanded=False)
                msg = friendly_error(exc)
                st.error(msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": f"⚠️ {msg}", "agent": "System", "workflow": steps}
                )
