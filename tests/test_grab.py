import unittest
from ddf_schedule import grab_ddf_sched


class TestGrab(unittest.TestCase):
    def test_grab(self):
        array = grab_ddf_sched()
        assert len(array) > 0


if __name__ == "__main__":
    unittest.main()
