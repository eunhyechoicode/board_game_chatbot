
from setuptools import setup, find_packages

setup(
    name="board_game_chatbot",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit",
        "python-dotenv",
        "openai",
        "langchain",
        "langchain-openai",
        "pinecone-client",
        "langsmith",
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
        ],
    },
    python_requires=">=3.9",
)