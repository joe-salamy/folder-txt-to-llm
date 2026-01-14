import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from actions import process_files

# Import configuration
from config import *

# Load environment variables from .env file
load_dotenv()


def main():
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file")
        print("Please create a .env file with: GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)

    # Get prompt file path
    script_dir = Path(__file__).parent
    prompt_file = script_dir / "prompts" / PROMPT_FILE

    # Validate prompt file
    if not prompt_file.exists():
        print(f"Error: Prompt file '{PROMPT_FILE}' not found at '{prompt_file}'")
        sys.exit(1)

    print(f"System prompt loaded from: {prompt_file}")
    print("=" * 60)
    print("PROCESSING FILES")
    print("=" * 60 + "\n")

    # Process files from the single input folder
    process_files(prompt_file, api_key)

    print("\n" + "=" * 60)
    print("Processing complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
