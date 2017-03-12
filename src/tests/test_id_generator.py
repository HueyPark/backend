from framework.id_generator import IdGenerator
from time import time


class TestIdGenerator:
    def test_generate(self):
        timestamp = int(time())
        id_generator = IdGenerator()
        uuid = id_generator.generate_by_time(timestamp)
        timestamp_from_id = id_generator.get_time(uuid)
        assert timestamp == timestamp_from_id

    def test_generate_multi(self):
        ids = set()
        id_generatpr = IdGenerator()
        for _ in range(100000):
            uuid = id_generatpr.generate()
            assert uuid not in ids

            ids.add(uuid)

    def test_generate_by_tim_nulti(self):
        ids = set()
        id_generatpr = IdGenerator()
        timestamp = int(time())
        for _ in range(100000):
            uuid = id_generatpr.generate_by_time(timestamp)
            assert uuid not in ids

            ids.add(uuid)
