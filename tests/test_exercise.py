import pytest
from src.gauge import Guage

def test_exercise(capsys):
    g = Gauge()

    while(!g.full()):
        print("Not full! Value: " + g.value())
        g.increase()

    print("Full! Value: " + g.value())
    g.decrease()
    print("Not full! Value: " + g.value())

    out, err = capsys.readouterr()
    assert out == "Not full! Value: 0\nNot full! Value: 1\nNot full! Value: 2\nNot full! Value: 3\nNot full! Value: 4\nFull! Value: 5\nNot full! Value: 4\n"
