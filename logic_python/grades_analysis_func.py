def grade_analysis(*grades, show_situation=False):
    grade_stats = {}
    grade_stats['total'] = len(grades)
    grade_stats['minimum'] = min(grades)
    grade_stats['maximum'] = max(grades)
    grade_stats['average'] = sum(grades) / len(grades)
    if show_situation:
        if grade_stats['average'] >= 6:
            grade_stats['situation'] = 'GOOD'
        elif grade_stats['average'] >= 5:
            grade_stats['situation'] = 'REASONABLE'
        else:
            grade_stats['situation'] = 'BAD'
    return grade_stats


grades = (3, 8, 5, 6)
grade_analysis_result = grade_analysis(*grades, show_situation=True)
print(grade_analysis_result)
