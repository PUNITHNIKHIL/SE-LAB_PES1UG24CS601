
import pytest
from self_storage import rent_due, access_allowed, payment_status


# ---------------- RENT DUE TEST CASES ----------------

def test_invalid_unit():
    with pytest.raises(ValueError):
        rent_due("extra", 5, False, False)


def test_negative_months():
    with pytest.raises(ValueError):
        rent_due("small", -1, False, False)


def test_small_unit_within_deposit():
    assert rent_due("small", 1, False, False) == 0


def test_medium_unit_within_deposit():
    assert rent_due("medium", 2, False, False) == 0


def test_large_unit_within_deposit():
    assert rent_due("large", 3, False, False) == 0


def test_member_extra_month():
    assert rent_due("small", 3, False, True) == 80


def test_non_member_extra_month():
    assert rent_due("small", 2, False, False) == 80


def test_climate_control():
    assert rent_due("medium", 4, True, False) == 240


def test_large_unit_rent():
    assert rent_due("large", 5, False, False) == 160


def test_large_unit_member():
    assert rent_due("large", 5, False, True) == 160


def test_long_term_normal():
    assert rent_due("small", 9, False, False) == 560


def test_long_term_climate():
    assert rent_due("small", 9, True, False) == 840


def test_long_term_member_climate():
    assert rent_due("small", 9, True, True) == 735


# ---------------- ACCESS ALLOWED TEST CASES ----------------

def test_owner_allowed():
    assert access_allowed(12, 4, True) is True


def test_owner_too_many_visitors():
    assert access_allowed(12, 5, True) is False


def test_owner_boundary_visitors():
    assert access_allowed(12, 4, True) is True


def test_early_access():
    assert access_allowed(5, 1, False) is False


def test_late_access():
    assert access_allowed(23, 1, False) is False


def test_early_boundary():
    assert access_allowed(6, 1, False) is True


def test_late_boundary():
    assert access_allowed(22, 2, False) is True


def test_normal_access():
    assert access_allowed(12, 2, False) is True


def test_too_many_visitors():
    assert access_allowed(12, 3, False) is False


# ---------------- PAYMENT STATUS TEST CASES ----------------

def test_autopay_current():
    assert payment_status(0, True, False) == "current"


def test_normal_current():
    assert payment_status(5, False, False) == "current"


def test_autopay_grace():
    assert payment_status(-1, True, False) == "grace"


def test_normal_grace():
    assert payment_status(0, False, False) == "grace"


def test_autopay_with_prior_late():
    assert payment_status(10, True, True) == "current"


def test_prior_late_grace():
    assert payment_status(0, True, True) == "grace"


def test_normal_prior_late():
    assert payment_status(5, False, True) == "grace"


def test_lien_status():
    assert payment_status(-6, False, True) == "lien"
