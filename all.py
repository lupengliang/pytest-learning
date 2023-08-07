import pytest

# 建议干掉pytest.ini, 会有干拢
if __name__ == '__main__':
   pytest.main(["-sv", "./testwhite::test_hum::TestHum::test_01_dafashi", "-n=1"])