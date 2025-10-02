from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import FrameBreak

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
    canvas.rect(0, 0, PAGE_WIDTH/2 - 50, PAGE_HEIGHT, fill=1, stroke=0)
    canvas.restoreState()

def create_cv(output_file):
    # --- Frame Setup (two columns) --- changing this will effect the text in left box
    # left_frame = Frame(40, 40, PAGE_WIDTH/2 - 50, PAGE_HEIGHT-80, id='left')
    # right_frame = Frame(PAGE_WIDTH/2, 40, PAGE_WIDTH/2 - 50, PAGE_HEIGHT-80, id='right')

    left_frame = Frame(40, 40, left_frame_width, PAGE_HEIGHT - 80, id='left')
    right_frame = Frame(40 + left_frame_width + 20, 40, right_frame_width, PAGE_HEIGHT - 80, id='right')

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
        fontSize=10,
        leading=14,      # line spacing (more readable)
        spaceAfter=6,    # gap between paragraphs
    )


    skills_style = ParagraphStyle(
        'Skills',
        parent=styles['Normal'],
        fontSize=10,
        leading=20,     # more space between lines
        spaceAfter=8,   # extra gap after each skill block
    )

    # --- Left Column (Personal Info, Skills, Education) ---
    story = []
    story.append(Paragraph("Vinay Thakur", title_style))
    story.append(Paragraph("Senior Technical Lead", body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Contact</b>", section_style))
    story.append(Paragraph("9703949619<br/> vinay.t1112@gmail.com<br/>linkedin.com/in/callmevt", body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Skills</b>", section_style))
    story.append(Paragraph("Python<br/>SQL<br/>Docker<br/>Kubernetes<br/>Azure<br/>ETL<br/>CI/CD", skills_style))
    

    # 🚨 This tells ReportLab to stop filling left frame and move to right frame
    story.append(FrameBreak())

    # --- Right Column (Profile & Experience) ---
    story.append(Paragraph("<b>Profile</b>", section_style))
    story.append(Paragraph(
        "Senior Technical Engineer with 13+ years of experience in data engineering, automation, "
        "and cloud platforms. Skilled in designing large-scale systems, RPA, and leading teams "
        "through digital transformation initiatives.", body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Employment History</b>", section_style))
    story.append(Paragraph("<b>Senior Technical Lead</b>, Colt Technology Services (2023–Present)", body_style))
    story.append(Paragraph("Working on Docker, Kubernetes, Argo workflow, and AI/ML automation.", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Senior Backend Developer</b>, Colt Technology Services (2021–2023)", body_style))
    story.append(Paragraph("Led migrations, built pipelines, and developed automation tools in Python/Java.", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Backend Developer</b>, Colt Technology Services (2016–2020)", body_style))
    story.append(Paragraph("Created XML processing tools, backend automation, and reporting systems.", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Operations Engineer</b>, TCS (2012–2016)", body_style))
    story.append(Paragraph("Managed server ops, billing automation, and infra support.", body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Education</b>", section_style))
    story.append(Paragraph("B.Tech, BPUT (2007–2011)", body_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Courses</b>", section_style))
    story.append(Paragraph("AIML PGP, Upgrad (Aug 2022 – Nov 2023)", body_style))

    # Build PDF
    doc.build(story)
    print(f"CV generated: {output_file}")

# Run
create_cv("Vinay_Thakur_CV.pdf")