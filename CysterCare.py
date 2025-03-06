from lamini import Lamini
import os
import json
from dotenv import load_dotenv
import lamini
from datasets import load_dataset
import jsonlines

load_dotenv()

try:
    api_key = os.getenv("LAMINI_API_KEY")
    print("LAMINI_API_KEY:", api_key)
    lamini.api_key = api_key
except Exception as e:
    print("No key found. API error")
    raise e

def get_data(file_path):
    data = []
    with jsonlines.open(file_path) as reader:
        for obj in reader:
            data.append(obj)
    return data

file_path = 'pcos_chatbot_training.jsonl'
data = get_data(file_path)

# print("Initializing LLM...")
# llm = Lamini(model_name="meta-llama/Meta-Llama-3.1-8B-Instruct")

# print("Starting training...")
# llm.train(
#     data_or_dataset_id=data*10,
#     finetune_args={"max_steps": 100, "learning_rate": 1e-4},
#     gpu_config={"gpus": 1, "nodes": 2}
# )
# print("Training initiated.")


# For text generation after tuning the llm
llm = Lamini(model_name="8b11ee2058ec232b293a8fcbf798841c34a2a1efc19698ae1ef3682722046b18")
print(llm.generate("""<|begin_of_text|><|start_header_id|>user<|end_header_id|>

What is PCOS?<|eot_id|>
<|start_header_id|>assistant<|end_header_id|>

"""))
print("Training Executed.")