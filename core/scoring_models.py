def security_risk(encryption, audit_logs, pii_protection):
    score = 100
    if encryption:
        score -= 30
    if audit_logs:
        score -= 30
    if pii_protection:
        score -= 20
    return max(0, score)

def compliance_risk(gdpr, soc2, iso27001):
    score = 100
    if gdpr:
        score -= 30
    if soc2:
        score -= 30
    if iso27001:
        score -= 30
    return max(0, score)

def cost_risk(monthly_cost, budget):
    ratio = monthly_cost / budget if budget > 0 else 1
    if ratio <= 0.5:
        return 20
    elif ratio <= 1:
        return 50
    return 90

def lockin_risk(open_source, exportable):
    score = 100
    if open_source:
        score -= 50
    if exportable:
        score -= 30
    return max(0, score)