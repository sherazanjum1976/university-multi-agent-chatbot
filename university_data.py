"""
Knowledge base for COMSATS University Islamabad (CUI), Wah Campus.

HOW THIS WAS BUILT: cuiwah.edu.pk blocks automated reading of most pages, so this
file uses (a) facts visible on the public cuiwah.edu.pk pages/search snippets and
(b) clearly-marked third-party estimates. Items marked [VERIFY] should be checked
against https://cuiwah.edu.pk before relying on them. Edit the text below freely;
the agents only answer from what is written here.
Last updated: September 2026.
"""

UNIVERSITY_NAME = "COMSATS University Islamabad (CUI), Wah Campus"
WEBSITE = "https://cuiwah.edu.pk"

ADMISSIONS = {
    "Admission policy": "Merit-based admissions for students from all backgrounds. Applications are submitted online through the CUI admission portal (see https://cuiwah.edu.pk, Admissions section).",
    "Intakes": "Two intakes per year: Spring and Fall (Fall is the main intake). Exact dates change every year; check the admission portal.",
    "Application deadline (latest known)": "For Fall 2026 the Wah campus closing date was reported as 11 August 2026 (third-party source, [VERIFY]). Fall 2026 has passed; for the next intake (Spring 2027) watch cuiwah.edu.pk for the announcement.",
    "Entry test": "Applicants are reported to need a valid NTS NAT (National Aptitude Test) score; those who have not taken it can register for the NTS test (third-party source, [VERIFY]).",
    "Engineering eligibility (from CUI Wah undergraduate page)": "Intermediate (HS/HSSC/A-level) Pre-Engineering with Physics, Mathematics and Chemistry with minimum 60% marks, OR DAE in the same/relevant field with minimum 60% marks, OR Intermediate with ICS (Physics, Mathematics, Computer Science/Computer Studies) with minimum 60% marks. Other conditions approved by the competent authority and the Pakistan Engineering Council also apply.",
    "Other programs eligibility": "Each program has its own criteria. Details are in the Undergraduate Prospectus on cuiwah.edu.pk (Admissions > Prospectus).",
    "Application steps (general CUI process)": [
        "Take/register for the NTS NAT test if you do not already have a valid score",
        "Apply online through the CUI admission portal and select Wah campus and your program preferences",
        "Upload the required documents and pay the application processing fee",
        "Check the merit list; if selected, download the offer letter",
        "Pay the first semester fee to confirm the seat",
    ],
    "Documents": "Typically educational certificates/transcripts, CNIC or B-Form, photographs and test result. The exact list is in the prospectus and admission portal [VERIFY].",
    "Where to get official details": "Undergraduate Prospectus and admission notices on https://cuiwah.edu.pk, or contact the Wah campus admission office.",
}

FEES = {
    "Official fee structure (Fall 2025 session, subject to revision)": {
        "Admission fee": "Rs. 22,000 one-time, charged to new entrants in addition to the semester fee",
        "Per credit hour fee (additional semesters, Undergraduate and Masters programs)": "Rs. 6,000 per credit hour",
        "Per credit hour fee (additional semesters, MS/PhD programs)": "Rs. 4,000 per credit hour",
        "Registration fee": "Charged for each additional semester in addition to the per-credit-hour fee",
        "Degree fee": "Rs. 10,000 on completion/award of the degree",
        "Note": "Fee rates are subject to revision in subsequent semesters. The full fee page is at https://cuiwah.edu.pk/fee-structure.aspx",
    },
    "First-semester total": "The exact first-semester total per program is not included in this knowledge base. Please check the fee structure page or the admission office.",
    "Unofficial estimates (third-party websites, not from CUI, [VERIFY])": {
        "Typical semester cost at Wah and similar campuses": "roughly Rs. 110,000 to 125,000 per semester (engineering/computing)",
        "Other one-time charges reported": "Endowment fund about Rs. 5,000; refundable caution money about Rs. 5,000",
        "Hostel (where available)": "about Rs. 5,000 one-time plus Rs. 30,000 to 40,000 per semester, excluding food",
    },
    "Overseas / international students": "Different fee structures apply; ask the admission office.",
    "Scholarships": "Merit-based tuition waivers and government schemes (for example the Ehsaas Undergraduate Scholarship) are commonly available to CUI students. Exact criteria for Wah are not in this knowledge base [VERIFY].",
    "Where to get official details": "https://cuiwah.edu.pk/fee-structure.aspx or the campus accounts/admission office.",
}

PROGRAMS = {
    "Overview": "CUI Wah Campus has 8 academic departments. The current prospectus lists 22 offered programs in total: 5 undergraduate, 11 MS and 6 PhD (as shown on the prospectus page; an older page listed 28 programs, so [VERIFY] the current list).",
    "Academic departments": [
        "Computer Science (Computing)",
        "Computer Engineering",
        "Electrical Engineering",
        "Mechanical Engineering",
        "Civil Engineering",
        "Management Sciences",
        "Mathematics",
        "Humanities",
    ],
    "Program levels": "BS (undergraduate), MS and PhD. The engineering programs are subject to Pakistan Engineering Council (PEC) requirements.",
    "Reported (unofficial) program": "BS Artificial Intelligence has been reported at Wah by a third-party guide [VERIFY].",
    "Eligibility": "Engineering: FSc Pre-Engineering (or DAE, or ICS with Physics, Mathematics, Computer Science) with minimum 60%. Other programs: see prospectus.",
    "Labs": "Major laboratories include Electronics, Microprocessor, VLSI and DSP laboratories; 51 fully equipped laboratories in total.",
    "Course catalog": "Public course catalog: http://cuonline.comsats.edu.pk/publicaccess/",
    "Prospectus": "Undergraduate Prospectus is available on https://cuiwah.edu.pk under Admissions > Prospectus.",
    "Careers": "Detailed career information per program is not in this knowledge base. CUI Wah runs research and commercialization activity through its Office of Research, Innovation and Commercialization (ORIC).",
}

GENERAL = {
    "About": "COMSATS University Islamabad (CUI) Wah Campus was established in 2001 and is one of the seven CUI campuses in Pakistan. It has over 3,000 students (3,289 enrolled per the campus academic page) and nearly 200 faculty members.",
    "Leadership": "Director of the Wah Campus: Prof. Dr. Samina Nawab. Rector of CUI: Prof. Dr. Raheel Qamar.",
    "Location": "Wah Cantonment, Punjab, Pakistan (Quaid Avenue, Wah Cantt) [VERIFY exact address on the website].",
    "Classrooms": "All lecture rooms are IT-enabled, air-conditioned and well furnished.",
    "Library": "About 25,000 library books plus a library portal.",
    "Labs": "51 fully equipped laboratories; major ones are Electronics, Microprocessor, VLSI and DSP labs.",
    "Hostel": "Hostel facility for about 300 male/female students.",
    "Transport": "Transport is provided on specified routes from Islamabad, Rawalpindi and Attock, with 10 buses of 64 seats.",
    "Cafeteria": "Food-street style catering with shops and kiosks offering a range of snacks and meals.",
    "Sports": "Sports is an integral part of extracurricular activities at the campus.",
    "Safety": "The campus states that student safety is its top concern.",
    "Research": "Office of Research, Innovation and Commercialization (ORIC). Figures shown on the campus site: 2,269 journal papers, 385 conference papers, 53 book chapters, 93 funded projects, 90 IGNITE funded projects and 28 patents.",
    "Rankings (CUI as a whole)": "THE World University Rankings 2026: 601-800 band, ranked #2 in Pakistan among listed universities as shown on the campus site; THE Impact Rankings: 17 of 17 SDGs, #1 in Pakistan (2024).",
    "Student portals": "CUOnline (student portal), Course Catalogue, Library Portal, Microsoft for all, UNESCO Water Chair, IRC.",
    "Contact": "Use the contact section of https://cuiwah.edu.pk for official phone numbers and email addresses.",
}


def to_text(data, indent=0):
    """Convert nested dict/list data into plain text (no curly braces, safe for CrewAI)."""
    pad = "  " * indent
    lines = []
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                lines.append(f"{pad}- {key}:")
                lines.append(to_text(value, indent + 1))
            else:
                lines.append(f"{pad}- {key}: {value}")
    elif isinstance(data, list):
        for item in data:
            lines.append(f"{pad}- {item}")
    else:
        lines.append(f"{pad}{data}")
    return "\n".join(lines)


def build_prompt(topic, data, query, history=""):
    """Shared prompt for all specialist agents."""
    safe_query = query.replace("{", "(").replace("}", ")")
    safe_history = history.replace("{", "(").replace("}", ")")
    return (
        f"You are the assistant for {UNIVERSITY_NAME}, answering prospective and current students.\n"
        f"Topic: {topic}\n\n"
        f"KNOWLEDGE BASE:\n{to_text(data)}\n\n"
        f"RECENT CONVERSATION:\n{safe_history or 'None'}\n\n"
        f"STUDENT QUESTION: {safe_query}\n\n"
        "RULES:\n"
        "- Answer ONLY using the knowledge base above.\n"
        "- If the answer is not in the knowledge base, say you do not have that detail and point the student to https://cuiwah.edu.pk or the campus office.\n"
        "- Items marked [VERIFY] or 'unofficial' must be presented as approximate, and tell the student to confirm on the official website.\n"
        "- Fees and dates change every semester; remind the student to confirm on the official website.\n"
        "- Be friendly, clear and concise. Use short bullet points when helpful.\n"
        "- Never invent numbers, dates, program names or policies."
    )
