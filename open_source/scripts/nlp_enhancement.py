python
from transformers import pipeline

# Load pre-trained model for text generation
generator = pipeline('text-generation', model='gpt-3')

# Generate text
def generate_text(prompt, max_length=50):
    return generator(prompt, max_length=max_length, num_return_sequences=1)

if __name__ == "__main__":
    prompt = "The future of AI is"
    generated_text = generate_text(prompt)
    print(f"Generated text: {generated_text}")
