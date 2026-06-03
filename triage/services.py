def calculate_priority(temperature, oxygen_level, pulse_rate, symptoms=""):

    symptoms = symptoms.lower()

    # CRITICAL RULES
    if oxygen_level and oxygen_level < 90:
        return "CRITICAL"

    if "unconscious" in symptoms:
        return "CRITICAL"

    if "chest pain" in symptoms:
        return "CRITICAL"

    # HIGH RULES
    if temperature and temperature >= 39:
        return "HIGH"

    if oxygen_level and oxygen_level < 94:
        return "HIGH"

    if pulse_rate and pulse_rate > 120:
        return "HIGH"

    # MEDIUM RULES
    if temperature and temperature >= 37.5:
        return "MEDIUM"

    # DEFAULT
    return "LOW"