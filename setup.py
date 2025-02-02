from setuptools import setup, find_packages

setup(
    name="climate",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pyfiglet",
        "requests",
        "simple_chalk",
        "tabulate",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "climate = CLImate.main:main",  
        ]
    },
    author="Sarath Madhav",
    description="A terminal weather app",
    url="https://github.com/Pseudozoid/CLImate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)

