import os
import shutil
from pathlib import Path


def janitor() -> None:
    download_folder = Path.home() / "Downloads"

    for file_path in download_folder.iterdir():
        if file_path.is_file():
            extension = file_path.suffix.lower()

            if extension == ".pdf":
                dest_folder = Path.home() / "Documents" / "PDFs"

                os.makedirs(dest_folder, exist_ok = True)
                shutil.move(str(file_path), str(dest_folder / file_path.name))

if __name__ == "__main__":
    janitor()