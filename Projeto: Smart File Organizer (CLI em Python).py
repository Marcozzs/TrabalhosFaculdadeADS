import os
import shutil
import sys
from collections import defaultdict

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".java", ".html", ".css", ".json"],
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"

def organize_folder(path):
    if not os.path.isdir(path):
        print("❌ Pasta inválida")
        return

    stats = defaultdict(int)

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            category = get_category(ext)

            target_dir = os.path.join(path, category)
            os.makedirs(target_dir, exist_ok=True)

            shutil.move(file_path, os.path.join(target_dir, file))
            stats[category] += 1

    print("\n📦 Organização concluída:\n")
    for category, count in stats.items():
        print(f"✔ {count} arquivo(s) em {category}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python organizer.py <caminho_da_pasta>")
    else:
        organize_folder(sys.argv[1])
