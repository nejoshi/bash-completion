import pytest


class Test(object):

    @pytest.mark.complete("smbcacls -")
    def test_dash(self, completion):
        assert completion.list