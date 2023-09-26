from setuptools import setup, find_packages

setup(
    name="Master_DE_Scaper_packages",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "Master-DE-Scaper.py = linkedin_scraper.main:run_linkedin_scraper"
        ]
    }
)
