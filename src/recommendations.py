def get_recommendations(result):

    recommendations = []

    if not result["length"]:
        recommendations.append("Use at least 8 characters.")

    if not result["uppercase"]:
        recommendations.append("Add at least one uppercase letter.")

    if not result["lowercase"]:
        recommendations.append("Add at least one lowercase letter.")

    if not result["digit"]:
        recommendations.append("Add at least one digit.")

    if not result["special"]:
        recommendations.append("Add at least one special character.")

    return recommendations