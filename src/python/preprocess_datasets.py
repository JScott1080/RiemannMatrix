import os
import subprocess

def preprocess_datasets(voice_name):
    raw_dataset_path =  f"data/Datasets/{voice_name}"
    preprocessed_dataset_path = f"data/Preprocessed/{voice_name}"

    #ensure the preprocessed dataset directory exists
    os.makedirs(preprocessed_dataset_path, exist_ok=True)

    #run the preprocessing script
    command = [
        "python", "TTS/bin/preprocess.py",
        "--input_dir", raw_dataset_path,
        "--output", preprocessed_dataset_path,
    ]

    subprocess.run(command, check=True)
    print(f"Preprocessing completed for voice {voice_name}!")

if __name__ == "__main__":
    voices = ["FLC", "CTN", "RDL"]

    for voice in voices:
        print(f"Preprocessing voice {voice}...")
        preprocess_datasets(voice)
