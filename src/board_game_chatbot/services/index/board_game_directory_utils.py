import os
from pathlib import Path
from functools import lru_cache
from board_game_chatbot.config.model_config import load_config


def get_project_root() -> Path:
    """Get the project root directory.

    Returns:
        Path: The absolute path to the project root directory
    """
    current_file = Path(__file__).resolve()
    return current_file.parents[4]  # Go up 4 levels to reach the root directory


@lru_cache()
def get_base_directory():
    """Get the base directory for board games."""
    config = load_config()
    relative_path = config['paths']['board_games_dir']
    project_root = get_project_root()
    absolute_path = os.path.join(project_root, relative_path)
    return absolute_path


def list_board_game_indices():
    """List all board game directories in the base directory."""
    base_directory = get_base_directory()
    if not os.path.exists(base_directory):
        print(f"Directory does not exist: {base_directory}")
        return []

    try:
        contents = os.listdir(base_directory)
        return [folder for folder in contents
                if os.path.isdir(os.path.join(base_directory, folder))]
    except Exception as e:
        print(f"Error while listing directory: {e}")
        return []