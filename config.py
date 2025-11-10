from pathlib import Path

# Maximum number of concurrent workers for processing files
MAX_WORKERS = 5

# Model configuration
MODEL_TYPE = "gemini-2.5-pro"

# Prompt configuration
PROMPT_FILE = "wa3-cases.md"  # Change this to the desired prompt file name (e.g., "reading.md", "lecture.md")

# Folder structure configuration
INPUT_FOLDER_NAME = "C:\\Users\\joesa\\OneDrive\\Documents\\Law school\\LRW\\WA3\\Precedent cases\\txt"  # Name of the input folder in each class directory
OUTPUT_FOLDER_NAME = (
    "C:\\Users\\joesa\\Downloads"  # Name of the output folder in each class directory
)
