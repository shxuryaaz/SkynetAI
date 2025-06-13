from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_name = "mistralai/Mistral-7B-Instruct-v0.1"

# Load model + tokenizer once
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"  # Will auto-use GPU if available
)

# Create pipeline
chat_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=512,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.9
)

def generate_response(query, domain="general"):
    # Optional: Add domain to system prompt
    system_prompt = {
        "general": "You are a helpful assistant.",
        "finance": "You are a finance expert. Explain things simply.",
        "medical": "You are a doctor. Answer medical questions clearly.",
        "legal": "You are a legal advisor. Provide simple explanations."
    }.get(domain, "You are a helpful assistant.")

    prompt = f"<s>[INST] {system_prompt} {query} [/INST]"

    result = chat_pipeline(prompt)[0]["generated_text"]
    
    # Extract only the reply after the prompt
    return result.replace(prompt, "").strip()
