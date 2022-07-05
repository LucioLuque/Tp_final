import pytest
from synthesizer import *
from note import *
from modulation import *

def test_get_frequency():
    with pytest.raises((KeyError,TypeError)):
        assert Synthesizer(440,"queen.txt", "piano.txt").get_frequency("AAA")
        assert Synthesizer(440,"queen.txt", "piano.txt").get_frequency(440)

def test_create_note():
    with pytest.raises(TypeError):
        assert Synthesizer(440,"queen.txt", "paino.txt").create_note("sss")
        assert Synthesizer(440,"queen.txt", "paino.txt").create_note(None)

def test_create_armonic_note():
    with pytest.raises(TypeError):
        assert ArmonicNote().get_armonic("sss")

def test_array_of_note():
    with pytest.raises(TypeError):
        assert CreateArrayNote("aaaa","ppppp").array_of_note()

def test_modulation():
    with pytest.raises(TypeError):
        assert CONSTANT("A",1111)
        assert LINEAR("aaa",None)
        assert INVLINEAR("I",999)
        assert SIN([],"FF")
        assert EXP([222],[0])
        assert INVEXP("ssss",11)
        assert QUARTCOS("yyy","yyyy")
        assert QUARTSIN(22,22)
        assert HALFCOS("A",1111)
        assert HALFSIN("aaa",None)
        assert LOG("I",999)
        assert INVLOG([],"FF")
        assert TRI([222],[0])
        assert PULSES("ssss",11)

def test_read_instrument():
    with pytest.raises(TypeError):
        assert ReadInstrument("test_instrument_pytest.txt").read()
        assert ReadInstrument("test_pytest_read_instrument").read()

def test_read_partiture():
    with pytest.raises(TypeError):
        assert ReadPartiture("text_proof_pytest.txt").read_partiture()
        assert ReadPartiture("text_proof_pytest_read_partiture").read_partiture()
       
if __name__ == "__main__":
    pytest.main()