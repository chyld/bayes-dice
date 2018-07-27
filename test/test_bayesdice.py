from src.bayesdice import BayesDice
from pytest import approx


def test_class_works():
    bd = BayesDice()
    assert isinstance(bd, BayesDice)
    assert sum(bd.data.values()) == 1


def test_choose_die():
    bd = BayesDice()
    bd.choose_die()
    assert bd.die in [4, 6, 8, 12, 20]


def test_roll_die():
    bd = BayesDice()
    bd.choose_die()
    roll = bd.roll_die()
    assert roll in range(1, bd.die + 1)


def test_update_priors():
    bd = BayesDice()
    bd.die = 8
    bd.update_priors(4)
    assert bd.data[4] == approx(0.37, rel=1e-1)
    assert bd.data[8] == approx(0.18, rel=1e-1)
    assert bd.data[20] == approx(0.07, rel=1e-1)
    bd.update_priors(7)
    assert bd.data[4] == approx(0.00, rel=1e-1)
    assert bd.data[8] == approx(0.62, rel=1e-1)
    assert bd.data[20] == approx(0.10, rel=1e-1)
