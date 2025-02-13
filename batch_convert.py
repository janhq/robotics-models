import argparse
from pathlib import Path
from typing import Iterator
import sys
from convert import main as convert_single_file


def find_robot_files(directory: Path) -> Iterator[Path]:
    """Recursively find all URDF and XML files in the given directory."""
    for path in directory.rglob("*"):
        if path.is_file() and path.suffix.lower() in [".urdf", ".xml"]:
            yield path


def get_output_basename(file_path: Path) -> str:
    """
    Generate a unique output basename that includes the original extension.
    For example:
        robot.urdf -> robot_urdf
        robot.xml -> robot_xml
    """
    # Remove the leading dot from suffix and convert to lowercase
    ext = file_path.suffix[1:].lower()
    # Combine stem and extension
    return f"{file_path.stem}_{ext}"


def process_directory(input_dir: str) -> None:
    """
    Process all robot description files in the input directory and its subdirectories.
    Creates a 'desc' folder in the same directory as each source file.
    Handles filename collisions by including the original file extension in output names.

    Args:
        input_dir: Path to the input directory
    """
    input_path = Path(input_dir).resolve()

    # Find all robot description files
    robot_files = list(find_robot_files(input_path))

    if not robot_files:
        print(f"No URDF or XML files found in {input_dir}")
        return

    print(f"Found {len(robot_files)} robot description files")

    # Process each file
    for file_path in robot_files:
        try:
            output_dir = file_path.parent / "desc"
            output_dir.mkdir(exist_ok=True)

            # Store the original name for the converter
            original_output_dir = output_dir

            # Create a temporary directory with the unique base name
            # This ensures the converter creates files with our desired naming scheme
            temp_output_dir = output_dir / get_output_basename(file_path)
            temp_output_dir.mkdir(exist_ok=True)

            print(f"\nProcessing: {file_path.relative_to(input_path)}")
            print(f"Output directory: {output_dir}")

            # Store original sys.argv
            original_argv = sys.argv

            # Modify sys.argv to match what convert.py expects
            sys.argv = [
                "convert.py",
                str(file_path),
                "--output-dir",
                str(temp_output_dir),
            ]

            try:
                convert_single_file()

                # Move files from temp directory to output directory with correct names
                for temp_file in temp_output_dir.glob("*"):
                    # Get the suffix (_config.md or _config.json)
                    config_suffix = temp_file.name.replace(file_path.stem, "")

                    # Create new filename with original extension included
                    new_name = get_output_basename(file_path) + config_suffix

                    # Move file to final destination
                    temp_file.rename(original_output_dir / new_name)

                # Remove temporary directory
                temp_output_dir.rmdir()

            finally:
                # Restore original sys.argv
                sys.argv = original_argv

        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description="Batch convert robot description files to Markdown and JSON. "
        "Creates an 'output' folder in the same directory as each source file."
    )
    parser.add_argument(
        "input_dir", type=str, help="Directory containing robot description files"
    )

    args = parser.parse_args()

    try:
        process_directory(args.input_dir)
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
