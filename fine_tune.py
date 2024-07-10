from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_NAME = "EleutherAI/gpt-j-6b"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
