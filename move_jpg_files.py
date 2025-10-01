import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    """
    Moves all .jpg files from source_folder to destination_folder.
    Creates the destination folder if it doesn't exist.
    Logs all moved files and total count.
    """
    # Ensure source exists
    if not os.path.exists(source_folder):
        print(f"❌ Source folder does not exist: {source_folder}")
        return

    # Ensure destination exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    files_moved = 0
    log_file = os.path.join(destination_folder, "moved_files_log.txt")

    with open(log_file, "w") as log:
        for root, _, files in os.walk(source_folder):
            for file in files:
                if file.lower().endswith(".jpg"):
                    src_path = os.path.join(root, file)
                    dst_path = os.path.join(destination_folder, file)
                    
                    # Handle duplicate filenames
                    if os.path.exists(dst_path):
                        base, ext = os.path.splitext(file)
                        count = 1
                        while os.path.exists(os.path.join(destination_folder, f"{base}_{count}{ext}")):
                            count += 1
                        dst_path = os.path.join(destination_folder, f"{base}_{count}{ext}")

                    shutil.move(src_path, dst_path)
                    log.write(f"{file} -> {dst_path}\n")
                    print(f"Moved: {file}")
                    files_moved += 1

    print(f"\n✅ Task completed. Total files moved: {files_moved}")
    print(f"Log saved as: {log_file}")


if __name__ == "__main__":
    print("=== Move all .jpg files ===")
    src = input("Enter source folder path: ").strip()
    dst = input("Enter destination folder path: ").strip()
    move_jpg_files(src, dst)
