from unittest import TestCase
import os

class TestCollect(TestCase):
    def test_get_scraper_list(self):
        scraper_dir = os.path.join(os.getcwd(),'tests/data/test_scraper_files')
        from src.collect import get_scraper_list
        scrapers = get_scraper_list(scraper_dir)

        # Only a single file is a valid scraper, and should therefor be returned.
        assert len(scrapers) == 1

