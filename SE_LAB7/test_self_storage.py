
from hypothesis import given, strategies as st
from self_storage import parse_rental, duration_average, payable_rent


@given(st.text() | st.none())
def test_parse_rental_no_unexpected_crash(s):
    try:
        result = parse_rental(s)
        assert isinstance(result, tuple)
        assert len(result) == 2
    except ValueError:
        pass


@given(st.text() | st.none())
def test_duration_average_no_unexpected_crash(s):
    try:
        result = duration_average(s)
        assert isinstance(result, int)
    except ValueError:
        pass


@given(st.text() | st.none())
def test_payable_rent_no_unexpected_crash(s):
    try:
        result = payable_rent(s)
        assert isinstance(result, (int, float))
        assert result >= 0
    except ValueError:
        pass
