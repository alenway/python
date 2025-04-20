from fpdf import FPDF

def get_numeric_input(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return value
        print("❌ Please enter numbers only.")

def get_user_input():
    print("Enter the following details for your resume:\n")
    user_data = {
        "name": input("Full Name: "),
        "email": input("Email: "),
        "phone": get_numeric_input("Phone Number: "),
        "address": input("Address: "),
        "summary": input("Professional Summary: "),
        "skills": input("Skills (comma-separated): ").split(","),
        "experience": [],
        "education": [],
        "projects": []
    }

    print("\n--- Work Experience ---")
    while True:
        company = input("Company Name: ")
        role = input("Role: ")
        duration = input("Duration (e.g., Jan 2020 - Dec 2022): ")
        description = input("Description: ")
        user_data["experience"].append({
            "company": company,
            "role": role,
            "duration": duration,
            "description": description
        })
        more = input("Add another experience? (yes/no): ").lower()
        if more != "yes":
            break

    print("\n--- Education ---")
    while True:
        institution = input("Institution Name: ")
        degree = input("Degree: ")
        year = get_numeric_input("Year of Graduation: ")
        user_data["education"].append({
            "institution": institution,
            "degree": degree,
            "year": year
        })
        more = input("Add another education detail? (yes/no): ").lower()
        if more != "yes":
            break

    print("\n--- Projects ---")
    while True:
        title = input("Project Title: ")
        desc = input("Project Description: ")
        link = input("Project Link (e.g., GitHub URL): ")
        user_data["projects"].append({
            "title": title,
            "description": desc,
            "link": link
        })
        more = input("Add another project? (yes/no): ").lower()
        if more != "yes":
            break

    return user_data

def create_resume(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    def add_section_title(title):
        pdf.set_font("Arial", "B", 14)
        pdf.set_fill_color(220, 220, 220)
        pdf.cell(0, 10, title, ln=True, fill=True)

    # Header
    pdf.set_font("Arial", "B", 24)
    pdf.cell(0, 10, data["name"], ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"Email: {data['email']} | Phone: {data['phone']}", ln=True, align="C")
    pdf.cell(0, 10, f"Address: {data['address']}", ln=True, align="C")
    pdf.ln(5)

    # Summary
    add_section_title("Professional Summary")
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, data["summary"])
    pdf.ln(3)

    # Skills
    add_section_title("Skills")
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, ", ".join(skill.strip() for skill in data["skills"]))
    pdf.ln(3)

    # Experience
    if data["experience"]:
        add_section_title("Work Experience")
        for exp in data["experience"]:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"{exp['role']} at {exp['company']} ({exp['duration']})", ln=True)
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(0, 10, exp["description"])
            pdf.ln(1)

    # Education
    if data["education"]:
        add_section_title("Education")
        for edu in data["education"]:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"{edu['degree']} - {edu['institution']} ({edu['year']})", ln=True)
        pdf.ln(3)

    # Projects
    if data["projects"]:
        add_section_title("Projects")
        for proj in data["projects"]:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, proj["title"], ln=True)
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(0, 10, proj["description"])
            pdf.set_text_color(0, 0, 255)
            pdf.cell(0, 10, proj["link"], ln=True, link=proj["link"])
            pdf.set_text_color(0, 0, 0)
            pdf.ln(2)

    pdf.output("Resume.pdf")
    print("\n✅ Resume has been created successfully as 'Resume.pdf'!")

if __name__ == "__main__":
    user_data = get_user_input()
    create_resume(user_data)
