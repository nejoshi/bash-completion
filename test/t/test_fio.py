import pytest


class TestFio(object):

    @pytest.mark.complete("fio ")
    def test_1(self, completion):
        assert completion.list

    @pytest.mark.complete("fio --")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("fio --debug=foo,")
    def test_3(self, completion):
        assert completion.list