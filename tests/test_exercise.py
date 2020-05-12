import pytest
from src.gauge import Gauge

def test_exercise(capsys):
    g = Gauge(0)

    while not g.full():
        print("Not full! Value: " + str(g.value))
        g.increase()

    print("Full! Value: " + str(g.value))
    g.decrease()
    print("Not full! Value: " + str(g.value))

    out, err = capsys.readouterr()
    assert out == "Not full! Value: 0\nNot full! Value: 1\nNot full! Value: 2\nNot full! Value: 3\nNot full! Value: 4\nFull! Value: 5\nNot full! Value: 4\n"
