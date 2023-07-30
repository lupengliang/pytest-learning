import pytest


class TestNe:

    def test_01_emolieshou(self):
        print("精灵族 恶魔猎手 激活")

    def test_02_delouyi(self):
        print("精灵族 德鲁伊 激活")

    @pytest.mark.usermanage
    def test_03_baihu(self):
        print("精灵族 白虎 激活")

    @pytest.mark.smoke
    def test_04_mawei(self):
        print("精灵族 玛维 激活")


    