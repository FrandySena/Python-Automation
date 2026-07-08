from pathlib import Path
from send2trash import send2trash

def cleaner() -> None:
    screenshots_folder = Path.home() / "Pictures" / "Screenshots"

    for file_path in screenshots_folder.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()

            if extension == ".png":
                send2trash(file_path)

if __name__ == "__main__":
    cleaner()