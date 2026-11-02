import sys
import os

def create_ats_pdf(output_path):
    # Standard PDF 1.4 A4 page: 595.28 x 841.89 pt
    # Printable area: Left 40pt, Right 40pt (Width 515.28pt), Top 40pt (801pt), Bottom 40pt
    
    commands = []
    
    # ── HEADER ──
    # Name in Dark Midnight Navy
    commands.append("0.07 0.11 0.20 rg") # #111C32
    commands.append("BT")
    commands.append("/F1 18 Tf") # Helvetica-Bold 18
    commands.append("40 802 Td")
    commands.append("(EKTA SINGH) Tj")
    commands.append("ET")
    
    # Headline in Cobalt Blue
    commands.append("0.42 0.56 0.90 rg") # #6C8FE6
    commands.append("BT")
    commands.append("/F1 9.5 Tf")
    commands.append("40 788 Td")
    commands.append("(Computer Science Engineering Student | Aspiring Software Developer) Tj")
    commands.append("ET")
    
    # Contact in dark grey
    commands.append("0.25 0.25 0.25 rg")
    commands.append("BT")
    commands.append("/F2 8.8 Tf") # Helvetica 8.8
    commands.append("40 774 Td")
    commands.append("(Hubli, Karnataka, India  |  ektasingh0987@gmail.com  |  1234500000) Tj")
    commands.append("ET")
    
    # Top divider rule in subtle blue
    commands.append("0.8 w 0.42 0.56 0.90 RG")
    commands.append("40 765 m 555 765 l S")
    
    cur_y = 750
    
    def add_heading(title, y):
        # Section title in Dark Navy with bottom thin rule
        cmds = []
        cmds.append("0.07 0.11 0.20 rg")
        cmds.append("BT")
        cmds.append("/F1 10 Tf")
        cmds.append(f"40 {y} Td")
        cmds.append(f"({title.upper()}) Tj")
        cmds.append("ET")
        cmds.append("0.5 w 0.75 0.80 0.90 RG")
        cmds.append(f"40 {y - 3} m 555 {y - 3} l S")
        return cmds, y - 14

    # 1. PROFESSIONAL SUMMARY
    h_cmds, cur_y = add_heading("Professional Summary", cur_y)
    commands.extend(h_cmds)
    
    commands.append("0.15 0.15 0.15 rg") # Dark body text
    summary_lines = [
        "Computer Science Engineering student at KLE Institute of Technology with foundational knowledge of programming,",
        "databases and web technologies. Interested in software development and problem-solving, with academic project",
        "experience in C++ and database management systems. Seeking an internship opportunity to apply classroom",
        "knowledge, gain practical industry experience and develop technical skills."
    ]
    for line in summary_lines:
        commands.append("BT")
        commands.append("/F2 8.6 Tf")
        commands.append(f"40 {cur_y} Td")
        commands.append(f"({line}) Tj")
        commands.append("ET")
        cur_y -= 11.2
    cur_y -= 5

    # 2. TECHNICAL SKILLS
    h_cmds, cur_y = add_heading("Technical Skills", cur_y)
    commands.extend(h_cmds)
    
    skills = [
        ("Programming Languages: ", "C, C++, Python, Java"),
        ("Web Technologies: ", "HTML"),
        ("Database: ", "SQL"),
        ("Areas of Interest: ", "Software Development, Data Structures and Algorithms, Artificial Intelligence.")
    ]
    for label, val in skills:
        commands.append("BT")
        commands.append("0.07 0.11 0.20 rg")
        commands.append("/F1 8.6 Tf")
        commands.append(f"40 {cur_y} Td")
        commands.append(f"({label}) Tj")
        commands.append("0.20 0.20 0.20 rg")
        commands.append("/F2 8.6 Tf")
        commands.append(f"({val}) Tj")
        commands.append("ET")
        cur_y -= 11.5
    cur_y -= 5

    # 3. ACADEMIC PROJECTS
    h_cmds, cur_y = add_heading("Academic Projects", cur_y)
    commands.extend(h_cmds)
    
    # Project 1: Car Rental System – C++
    commands.append("BT")
    commands.append("0.07 0.11 0.20 rg")
    commands.append("/F1 9 Tf")
    commands.append(f"40 {cur_y} Td")
    commands.append("(Car Rental System - C++) Tj")
    commands.append("ET")
    cur_y -= 11.5
    commands.append("BT")
    commands.append("0.20 0.20 0.20 rg")
    commands.append("/F2 8.6 Tf")
    commands.append(f"50 {cur_y} Td")
    commands.append("(- Developed an academic mini-project using C++ and explored object-oriented programming concepts) Tj")
    commands.append("ET")
    cur_y -= 11
    commands.append("BT")
    commands.append("0.20 0.20 0.20 rg")
    commands.append("/F2 8.6 Tf")
    commands.append(f"50 {cur_y} Td")
    commands.append("(  through a car rental system.) Tj")
    commands.append("ET")
    cur_y -= 13

    # Project 2: DBMS Expense Tracker
    commands.append("BT")
    commands.append("0.07 0.11 0.20 rg")
    commands.append("/F1 9 Tf")
    commands.append(f"40 {cur_y} Td")
    commands.append("(DBMS Expense Tracker) Tj")
    commands.append("ET")
    cur_y -= 11.5
    commands.append("BT")
    commands.append("0.20 0.20 0.20 rg")
    commands.append("/F2 8.6 Tf")
    commands.append(f"50 {cur_y} Td")
    commands.append("(- Developed an academic project focused on expense tracking and database management.) Tj")
    commands.append("ET")
    cur_y -= 13

    # Project 3: Rope Climbing Robot
    commands.append("BT")
    commands.append("0.07 0.11 0.20 rg")
    commands.append("/F1 9 Tf")
    commands.append(f"40 {cur_y} Td")
    commands.append("(Rope Climbing Robot) Tj")
    commands.append("ET")
    cur_y -= 11.5
    commands.append("BT")
    commands.append("0.20 0.20 0.20 rg")
    commands.append("/F2 8.6 Tf")
    commands.append(f"50 {cur_y} Td")
    commands.append("(- Worked on an engineering project involving the concept and development of a rope-climbing robot.) Tj")
    commands.append("ET")
    cur_y -= 15

    # 4. EDUCATION
    h_cmds, cur_y = add_heading("Education", cur_y)
    commands.extend(h_cmds)
    
    edu_items = [
        ("Bachelor of Engineering - Computer Science and Engineering", "KLE Institute of Technology, Hubli | 2024 - 2028"),
        ("Pre-University Course (PUC)", "Dr. R. B. Patil Mahesh PU College | 2024 | 93%"),
        ("Secondary School (CBSE)", "Chinmaya Vidyalaya English Primary School | 2022 | 87.2%")
    ]
    for deg, inst in edu_items:
        commands.append("BT")
        commands.append("0.07 0.11 0.20 rg")
        commands.append("/F1 8.8 Tf")
        commands.append(f"40 {cur_y} Td")
        commands.append(f"({deg}) Tj")
        commands.append("ET")
        cur_y -= 11
        commands.append("BT")
        commands.append("0.25 0.25 0.25 rg")
        commands.append("/F2 8.5 Tf")
        commands.append(f"50 {cur_y} Td")
        commands.append(f"({inst}) Tj")
        commands.append("ET")
        cur_y -= 13
    cur_y -= 2

    # 5. COURSES AND LEARNING EXPERIENCES
    h_cmds, cur_y = add_heading("Courses and Learning Experiences", cur_y)
    commands.extend(h_cmds)
    courses = [
        "- Capacity Planning",
        "- Artificial Intelligence",
        "- Basics of Data Structures and Algorithms"
    ]
    for c in courses:
        commands.append("BT")
        commands.append("0.20 0.20 0.20 rg")
        commands.append("/F2 8.5 Tf")
        commands.append(f"50 {cur_y} Td")
        commands.append(f"({c}) Tj")
        commands.append("ET")
        cur_y -= 11
    cur_y -= 5

    # 6. LANGUAGES
    h_cmds, cur_y = add_heading("Languages", cur_y)
    commands.extend(h_cmds)
    commands.append("BT")
    commands.append("0.20 0.20 0.20 rg")
    commands.append("/F2 8.6 Tf")
    commands.append(f"50 {cur_y} Td")
    commands.append("(English, Hindi, Kannada.) Tj")
    commands.append("ET")

    stream_content = "\n".join(commands)
    stream_bytes = stream_content.encode("latin1")
    stream_len = len(stream_bytes)

    objects = []
    objects.append("1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    objects.append("2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    objects.append("3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>\nendobj\n")
    objects.append(f"4 0 obj\n<< /Length {stream_len} >>\nstream\n{stream_content}\nendstream\nendobj\n")
    objects.append("5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>\nendobj\n")
    objects.append("6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\nendobj\n")

    header = "%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    offsets = []
    current_offset = len(header.encode("latin1"))

    body = ""
    for obj in objects:
        offsets.append(current_offset)
        obj_bytes = obj.encode("latin1")
        current_offset += len(obj_bytes)
        body += obj

    xref_offset = current_offset
    xref = f"xref\n0 {len(objects) + 1}\n0000000000 65535 f \n"
    for off in offsets:
        xref += f"{off:010d} 00000 n \n"

    trailer = f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"

    final_pdf_bytes = (header + body + xref + trailer).encode("latin1")
    with open(output_path, "wb") as f:
        f.write(final_pdf_bytes)
    print(f"Generated clean ATS PDF at {output_path} ({len(final_pdf_bytes)} bytes)")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "Ekta_Singh_Resume.pdf"
    create_ats_pdf(out)
