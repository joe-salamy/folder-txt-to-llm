from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import google.generativeai as genai
from dotenv import load_dotenv
import pypdf

# Import configuration
from config import *

# Load environment variables from .env file
load_dotenv()


def read_file(filepath):
    """Read and return the contents of a file.

    Supports: .txt, .md, .pdf
    """
    try:
        filepath = Path(filepath)

        # Handle PDF files
        if filepath.suffix.lower() == ".pdf":
            with open(filepath, "rb") as f:
                reader = pypdf.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text

        # Handle text files
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None


def process_file_with_gemini(txt_content, system_prompt, api_key):
    """Send content to Gemini 2.5 Pro and return the response."""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name=MODEL_TYPE, system_instruction=system_prompt
        )

        generation_config = genai.types.GenerationConfig(
            # response_mime_type="application/json",
        )

        response = model.generate_content(
            txt_content, generation_config=generation_config
        )
        return response.text
    except Exception as e:
        print(f"Error processing with Gemini: {e}")
        return None


def process_single_file(txt_file, output_folder, system_prompt, api_key, total_files):
    """Process a single file with Gemini."""
    try:
        # Read input file
        txt_content = read_file(txt_file)
        if txt_content is None:
            return False

        # Process with Gemini
        result = process_file_with_gemini(txt_content, system_prompt, api_key)
        if result is None:
            return False

        # Save output
        output_file = output_folder / f"{txt_file.stem}.md"
        # output_file = output_folder / f"{txt_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"    ✓ Saved: {output_file.name}")
        return True

    except Exception as e:
        print(f"    ✗ Error processing {txt_file.name}: {e}")
        return False


def process_files(prompt_file, api_key):
    """Process all files from the single input folder."""
    input_folder = Path(INPUT_FOLDER_NAME)
    output_folder = Path(OUTPUT_FOLDER_NAME)

    # Validate input folder
    if not input_folder.exists():
        print(f"Error: Input folder '{input_folder}' does not exist")
        return

    # Get all txt, md, and pdf files
    txt_files = (
        list(input_folder.glob("*.txt"))
        + list(input_folder.glob("*.md"))
        + list(input_folder.glob("*.pdf"))
    )
    if not txt_files:
        print(f"No txt, md, or pdf files found in input folder")
        return

    # Read system prompt
    system_prompt = read_file(prompt_file)
    if system_prompt is None:
        return

    # Create output folder if it doesn't exist
    output_folder.mkdir(parents=True, exist_ok=True)

    print(f"Found {len(txt_files)} file(s) to process")
    print(f"Input folder:  {input_folder}")
    print(f"Output folder: {output_folder}\n")
    print(f"Processing with {MAX_WORKERS} concurrent workers\n")

    # Process files in parallel
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = []
        for txt_file in txt_files:
            print(f"Queuing: {txt_file.name}")
            future = executor.submit(
                process_single_file,
                txt_file,
                output_folder,
                system_prompt,
                api_key,
                len(txt_files),
            )
            futures.append(future)

        # Wait for all tasks to complete
        for future in futures:
            future.result()

    print("\nCompleted processing all files.")
