"""DEMO / SAMPLE data for a FICTIONAL university. Replace with real info later."""

UNIVERSITY_NAME = "Northbridge University (DEMO)"

ADMISSIONS = {
    "Undergraduate eligibility": "High school diploma (or equivalent) with at least 60% marks.",
    "Postgraduate eligibility": "Relevant bachelor's degree with CGPA 2.5/4.0 or higher.",
    "Application process": [
        "Create an account on the admissions portal (demo: apply.northbridge.example)",
        "Fill in the online application form",
        "Upload documents and pay the application fee",
        "Take the entrance test (undergraduate) or attend an interview (postgraduate)",
        "Merit list is published; accepted students confirm by paying the admission fee",
    ],
    "Required documents": [
        "Previous academic transcripts and certificates",
        "National ID card / passport copy",
        "4 passport-size photographs",
        "Entrance test admit card",
    ],
    "Deadlines": {
        "Fall intake": "Applications close July 15, classes start September 1",
        "Spring intake": "Applications close December 10, classes start February 1",
    },
    "Entrance test": "Northbridge Aptitude Test (NAT): 100 MCQs in Math, English and Analytical Reasoning; passing score 40%.",
    "Admissions office": "admissions@northbridge.example, Mon-Fri 9am-4pm",
}

FEES = {
    "Application fee": "$25 (non-refundable)",
    "Admission fee": "$150 (one-time, at enrollment)",
    "Tuition per semester": {
        "Computer Science": "$1,800",
        "Business Administration": "$1,500",
        "Electrical Engineering": "$1,900",
        "Psychology": "$1,300",
        "MBA": "$2,200",
        "MS Computer Science": "$2,400",
    },
    "Other charges": "Library and lab fee $100 per semester; exam fee $50 per semester.",
    "Scholarships": {
        "Merit Scholarship": "50% tuition waiver for students scoring 85% or above",
        "Need-Based Aid": "Up to 30% waiver with income documents",
        "Sibling Discount": "10% off tuition for the second sibling",
        "Sports Scholarship": "25% waiver for national-level athletes",
    },
    "Payment options": "Bank transfer, credit/debit card, or 3 installments per semester (no interest).",
    "Refund policy": "Full tuition refund before classes start; 50% within the first two weeks; none afterwards.",
    "Accounts office": "fees@northbridge.example",
}

PROGRAMS = {
    "Faculty of Computing": {
        "BS Computer Science": "4 years. Eligibility: 60% in high school with Math. Careers: software engineer, data scientist, AI engineer.",
        "MS Computer Science": "2 years. Eligibility: BS in CS or related field. Careers: researcher, senior engineer, lecturer.",
    },
    "Faculty of Business": {
        "BBA": "4 years. Eligibility: any high school stream, 60% marks. Careers: marketing, finance, entrepreneurship.",
        "MBA": "2 years. Eligibility: bachelor's degree plus 2 years experience preferred. Careers: management, consulting.",
    },
    "Faculty of Engineering": {
        "BS Electrical Engineering": "4 years. Eligibility: 60% in high school with Physics and Math. Careers: power systems, electronics, telecom.",
    },
    "Faculty of Social Sciences": {
        "BS Psychology": "4 years. Eligibility: 55% in high school. Careers: counselor, HR specialist, researcher.",
    },
    "Academic system": "Semester-based; 2 semesters per year; 15 weeks each. Graduation requires CGPA 2.0/4.0 or higher.",
}

GENERAL = {
    "About": "Northbridge University is a fictional demo university founded in 1995, with about 8,000 students.",
    "Campus": "Green 60-acre campus with a central library, sports complex, cafeteria, and a medical center.",
    "Location": "123 Demo Street, Sampletown (fictional).",
    "Hostels": "Separate hostels for men and women. Approx. $80/month for shared rooms; apply after admission.",
    "Transport": "University shuttle runs between campus and the city center every 30 minutes.",
    "Facilities": "Wi-Fi campus, computer labs, digital library, career services, and clubs (robotics, debate, music).",
    "Library hours": "Mon-Sat 8am-10pm, Sunday 10am-6pm.",
    "Contact": "info@northbridge.example, +1-555-0100",
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
        f"You are answering for {UNIVERSITY_NAME}, a FICTIONAL demo university.\n"
        f"Topic: {topic}\n\n"
        f"KNOWLEDGE BASE (demo data):\n{to_text(data)}\n\n"
        f"RECENT CONVERSATION:\n{safe_history or 'None'}\n\n"
        f"STUDENT QUESTION: {safe_query}\n\n"
        "RULES:\n"
        "- Answer ONLY using the knowledge base above.\n"
        "- If the answer is not in the knowledge base, say so politely and suggest contacting the relevant office.\n"
        "- Be friendly, clear and concise. Use short bullet points when helpful.\n"
        "- Never invent numbers, dates or policies."
    )
