def sla_risk(uptime_percentage):
    if uptime_percentage >= 99.9:
        return 10
    elif uptime_percentage >= 99:
        return 40
    return 80