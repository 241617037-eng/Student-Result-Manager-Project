
def get_grade(mark):
    if mark >= 80:
        return "A+", 4.00
    elif mark >= 75:
        return "A", 3.75
    elif mark >= 70:
        return "A-", 3.50
    elif mark >= 65:
        return "B+", 3.25
    elif mark >= 60:
        return "B", 3.00
    elif mark >= 55:
        return "B-", 2.75
    elif mark >= 50:
        return "C+", 2.50
    elif mark >= 45:
        return "C", 2.25
    elif mark >= 40:
        return "D", 2.00
    return "F", 0.00

# Test Cases
tests = [
    (85, "A+", 4.00),
    (78, "A", 3.75),
    (72, "A-", 3.50),
    (67, "B+", 3.25),
    (62, "B", 3.00),
    (57, "B-", 2.75),
    (52, "C+", 2.50),
    (47, "C", 2.25),
    (42, "D", 2.00),
    (30, "F", 0.00)
]

for mark, expected_grade, expected_point in tests:
    result = get_grade(mark)
    assert result == (expected_grade, expected_point)

print("All 10 Tests Passed!")