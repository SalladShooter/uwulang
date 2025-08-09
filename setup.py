from setuptools import setup, find_packages

setup(
    name="uwulang",
    version="0.1.1",
    description="Uwulang - a cute uwu-ified Python based language",
    url="https://github.com/SalladShooter/uwulang",
    author="SalladShooter",
    entry_points={
        "console_scripts": [
            "uwu=uwulang.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
