import torch
from transformers import LlamaForCausalLM, LlamaTokenizer
from constants import LLM_MODEL_DIR

class LLMModel:
    def __init__(self, model_name="llama"):
        self.tokenizer = LlamaTokenizer.from_pretrained(LLM_MODEL_DIR)
        self.model = LlamaForCausalLM.from_pretrained(LLM_MODEL_DIR)

    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=100)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Example usage
if __name__ == "__main__":
    llm = LLMModel()
    prompt = "Hello, how are you?"
    response = llm.generate_response(prompt)
    print(response)
