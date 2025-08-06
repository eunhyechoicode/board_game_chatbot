from dotenv import load_dotenv
from board_game_chatbot.core.session import initialize_session_state
from board_game_chatbot.ui.layout import setup_page_config
from board_game_chatbot.core.chat import display_chat_history, handle_user_input

def main():
    """Main application entry point"""
    load_dotenv()

    initialize_session_state()
    setup_page_config()

    display_chat_history()
    handle_user_input()

if __name__ == "__main__":
    main()
