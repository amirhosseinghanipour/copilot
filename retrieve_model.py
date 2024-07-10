from huggingface_hub import hf_hub_download
import joblib

REPO_ID = "EleutherAI/gpt-j-6b"
FILENAME = "gpt-j-6b.joblib"

def load_model(repo_id: str, filename: str) -> None:
    model = joblib.load(hf_hub_download(repo_id, filename))
    return model

load_model(REPO_ID, FILENAME)