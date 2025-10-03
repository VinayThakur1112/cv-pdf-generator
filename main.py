from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import FrameBreak

NAME = "Vinay Thakur"
POSOTION = "Senior Technical Lead"
MOBILE_NO = "979"
EMAIL_ID = "vi@gmail.com"
LINKEDIN_ID = "linkedin.com/in/"
GITHUB_ID = "linkedin.com/in/"
SKILLS = ["SQL", "Python"]
PROFILE = ("Senior Technical Engineer with 13+ years of experience in data engineering, automation, "
        "and cloud platforms. Skilled in designing large-scale systems, RPA, and leading teams "
        "through digital transformation initiatives.")

EMPLOYMENT_HISTORY = [
    {
        "role": "Senior Technical Lead",
        "company": "Colt Technology Services",
        "duration": "2023–Present",
        "desc": "Working on Docker, Kubernetes, Argo workflow, and AI/ML automation."
    },
    {
        "role": "Senior Backend Developer",
        "company": "Colt Technology Services",
        "duration": "2021–2023",
        "desc": "Led migrations, built pipelines, and developed automation tools in Python/Java."
    },
    {
        "role": "Backend Developer",
        "company": "Colt Technology Services",
        "duration": "2016–2020",
        "desc": "Created XML processing tools, backend automation, and reporting systems."
    },
    {
        "role": "Operations Engineer",
        "company": "TCS",
        "duration": "2012–2016",
        "desc": "Managed server ops, billing automation, and infra support."
    }
]

EDUCATION = "B.Tech, BPUT (2007–2011)"
COURSES = "AIML PGP, Upgrad (Aug 2022 – Nov 2023)"

# Custom background color (very light green)
LIGHT_GREEN = colors.HexColor("#F0FFF0")  # Honeydew

# Page dimensions
PAGE_WIDTH, PAGE_HEIGHT = A4

# --- Frame Setup (two columns, slimmer left sidebar) ---
left_frame_width = 180   # shrink left section
right_frame_width = PAGE_WIDTH - left_frame_width - 60  # remaining width (accounting for margins)


def add_background(canvas, doc):
    canvas.saveState()
    # Draw green rectangle only in the left column
    canvas.setFillColor(LIGHT_GREEN)
    canvas.rect(0, 0, PAGE_WIDTH/2.5 - 50, PAGE_HEIGHT, fill=1, stroke=0)
    canvas.restoreState()


def create_cv(output_file):
    # --- Frame Setup (two columns) --- changing this will effect the text in left box
    # left_frame = Frame(40, 40, PAGE_WIDTH/2 - 50, PAGE_HEIGHT-80, id='left')
    # right_frame = Frame(PAGE_WIDTH/2, 40, PAGE_WIDTH/2 - 50, PAGE_HEIGHT-80, id='right')

    left_frame = Frame(20, 40, left_frame_width, PAGE_HEIGHT - 80, id='left')
    right_frame = Frame(20 + left_frame_width + 20, 40, right_frame_width, PAGE_HEIGHT - 80, id='right')

    template = PageTemplate(frames=[left_frame, right_frame], onPage=add_background)

    # Document setup
    doc = SimpleDocTemplate(
        output_file, pagesize=A4, 
        rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=30
    )
    doc.addPageTemplates([template])

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'Title', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor("#1a1a1a"), spaceAfter=14
    )
    section_style = ParagraphStyle(
        'Section', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor("#003366"), spaceAfter=6
    )
    
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=9,
        leading=14,      # line spacing (more readable)
        spaceAfter=6,    # gap between paragraphs
    )


    skills_style = ParagraphStyle(
        'Skills',
        parent=styles['Normal'],
        fontSize=9,
        leading=20,     # more space between lines
        spaceAfter=8,   # extra gap after each skill block
    )

    # --- Left Column (Personal Info, Skills, Education) ---
    story = []
    story.append(Paragraph(NAME, title_style))
    story.append(Paragraph(POSOTION, body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Contact</b>", section_style))
    story.append(Paragraph(MOBILE_NO+ "<br/>" +EMAIL_ID+ "<br/>" +LINKEDIN_ID, body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Skills</b>", section_style))
    for skill in SKILLS:
        story.append(Paragraph(f"• {skill}", body_style))
    

    # 🚨 This tells ReportLab to stop filling left frame and move to right frame
    story.append(FrameBreak())

    # --- Right Column (Profile & Experience) ---
    story.append(Paragraph("<b>Profile</b>", section_style))
    story.append(Paragraph(PROFILE, body_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Employment History</b>", section_style))
    for job in EMPLOYMENT_HISTORY:
        story.append(Paragraph(f"<b>{job['role']}</b>, {job['company']} ({job['duration']})", body_style))
        story.append(Paragraph(job['desc'], body_style))
        story.append(Spacer(1, 8))  # spacing between jobs
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Education</b>", section_style))
    story.append(Paragraph(EDUCATION, body_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("<b>Courses</b>", section_style))
    story.append(Paragraph(COURSES, body_style))

    # Build PDF
    doc.build(story)
    print(f"CV generated: {output_file}")

# Run
create_cv("Vinay_Thakur_CV.pdf")