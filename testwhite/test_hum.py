import pytest

class TestHum:

    def test_01_dafashi(self):
        print("人族：大法师 激活")

    @pytest.mark.usermanage
    def test_02_xuefashi(self):
        print("人族：血法师 激活")
        assert 1 == 2

    @pytest.mark.smoke
    def test_03_shanqiuzhiwang(self):
        print("人族： 山丘之王 激活")

    @pytest.mark.run(order=1)
    def test_04_shengqishi(self):
        print("人族：圣骑士 激活")
