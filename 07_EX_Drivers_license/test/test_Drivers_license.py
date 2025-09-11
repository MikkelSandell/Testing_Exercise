import pytest
from app.Drivers_license import evaluate_candidate

@pytest.mark.parametrize("theory, practical, expected", [
	# Decision table cases
	(85, 2, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}),
	(84, 2, {"license_granted": False, "repeat_theory": True, "repeat_practical": False, "extra_lessons": False}),
	(85, 3, {"license_granted": False, "repeat_theory": False, "repeat_practical": True, "extra_lessons": False}),
	(84, 3, {"license_granted": False, "repeat_theory": True, "repeat_practical": True, "extra_lessons": True}),
	# Boundary value analysis
	(84, 1, {"license_granted": False, "repeat_theory": True, "repeat_practical": False, "extra_lessons": False}),
	(85, 1, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}),
	(86, 2, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}),
	(86, 3, {"license_granted": False, "repeat_theory": False, "repeat_practical": True, "extra_lessons": False}),
	# Edge cases
	(0, 0, {"license_granted": False, "repeat_theory": True, "repeat_practical": False, "extra_lessons": False}),
	(100, 0, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}),
	(85, 0, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}),
	(85, -1, {"license_granted": False, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}), # Invalid practical
	(-1, 2, {"license_granted": False, "repeat_theory": True, "repeat_practical": False, "extra_lessons": False}), # Invalid theory
	(101, 2, {"license_granted": True, "repeat_theory": False, "repeat_practical": False, "extra_lessons": False}), # Invalid theory
])
def test_evaluate_candidate(theory, practical, expected):
	result = evaluate_candidate(theory, practical)
	assert result == expected
