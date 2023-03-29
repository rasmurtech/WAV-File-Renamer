import os
import sys


def rename_wav_files(folder_path):
    wav_files = [f for f in os.listdir(
        folder_path) if f.lower().endswith('.wav')]
    wav_files.sort()

    if len(wav_files) > 999:
        print("Error: More than 999 WAV files found in the folder. Please reduce the number of files.")
        sys.exit(1)

    for index, wav_file in enumerate(wav_files, start=1):
        new_name = f"{index:03d}.wav"
        old_path = os.path.join(folder_path, wav_file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed '{wav_file}' to '{new_name}'")


if __name__ == "__main__":
    folder_path = r"C:\Users\Rasim Muratovic\Desktop\output"
    rename_wav_files(folder_path)
