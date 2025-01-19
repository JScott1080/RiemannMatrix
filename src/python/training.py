from TTS.trainer import Trainer, TrainerArgs
from TTS.tts.configs.shared_configs import BaseDatasetConfig 
from TTS.tts.configs.glow_tts_config import GlowTTSConfig

def get_dataset_config(name, path):
    return BaseDatasetConfig(
        formatter="ljspeech:",
        meta_file_train="metadata.csv",
        path=path
    )

def get_glow_tts_config(dataset_config):
    return GlowTTSConfig(
        batch_size=32,
        eval_batch_size=16,
        num_loader_workers=4,
        run_eval=True,
        phenom_language="en-us",
        dataset=[dataset_config],
    )

def train_glow_tts(name, data_path, output_path):
    dataset_config = get_dataset_config(name, data_path)
    config = get_glow_tts_config(dataset_config)
    args = TrainerArgs(
        config = config,
        output_path = output_path,
        tts_model_name = "glow_tts"
    )
    trainer = Trainer(args)
    trainer.fit()

    if __name__ == "__main__":
        voices = {
            "FLC":{
                "data_path": "data/Preprocessed/FLC",
                "output_path": "models/FLC"    
            },
            "CTN":{
                "data_path": "data/Preprocessed/CTN",
                "output_path": "models/CTN"
            },
            "RDL":{
                "data_path": "data/Preprocessed/RDL",
                "output_path": "models/RDL"
            }

        }

        for name, paths in voices.items(): 
            print(f"Training voice {name}...") 
            train_voice(name, paths["data_path"], paths["output_path"]) 
            print(f"Training completed for voice {name}!")