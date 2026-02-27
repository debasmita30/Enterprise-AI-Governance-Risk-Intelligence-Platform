from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.lib.units import inch

def generate_pdf(tool_name, scores, final_score, category):

    file_path = f"{tool_name}_Governance_Report.pdf"
    doc = SimpleDocTemplate(file_path)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph(f"AI Governance Report - {tool_name}", styles["Heading1"]))
    elements.append(Spacer(1, 0.3 * inch))

    data = [["Risk Dimension", "Score"]]
    for k, v in scores.items():
        data.append([k, v])

    data.append(["Final Risk Score", final_score])
    data.append(["Risk Category", category])

    table = Table(data)
    elements.append(table)

    doc.build(elements)

    return file_path