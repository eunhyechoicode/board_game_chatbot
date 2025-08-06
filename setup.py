from setuptools import setup, find_packages

setup(
    name="board_game_chatbot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    # Test dependencies should be specified separately
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            # other test dependencies
        ],
    },
)
