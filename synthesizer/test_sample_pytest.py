# import unittest
import pytest
import synthesizer
import modulation

def test_get_frequency():
    with pytest.raises((KeyError,TypeError)):
        assert synthesizer.Synthesizer("queen.txt", "piano.txt").get_frequency("AAA")
        assert synthesizer.Synthesizer("queen.txt", "piano.txt").get_frequency(440)

if __name__ == "__main__":
    pytest.main()