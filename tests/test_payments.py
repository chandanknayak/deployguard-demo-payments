from services.payments import compute_fee


def test_compute_fee():
    assert compute_fee(1000) == 59
