import pytest

class TestSuite:

    @classmethod
    def setup_class(cls):
        print("Se ejecuta una sola vez al inicio")

    def setup_method(self):
        print("Se ejecuta ANTES de cada test case")

    @pytest.mark.smoke
    def test_first(self):
        print("Test first")
    
    @pytest.mark.regression
    def test_second(self):
        print("Test second")

    @pytest.mark.touch
    def test_third(self):
        print("Test third")

    def do_something(self):
        pass

    def teardown_method(selfs):
        print("Se ejecuta al FINAL de cada test case")

    @classmethod
    def teardown_class(cls):
        print("Se ejecuta una sola vez al final")