from src.bayesdice import BayesDice


def test_class_works():
    bd = BayesDice()
    assert isinstance(bd, BayesDice)
