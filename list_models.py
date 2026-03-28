from groq import Groq
import config   # make sure your GROQ_API_KEY is stored in config.py

# Initialize client
client = Groq(api_key=config.GROQ_API_KEY)

# List all models available to your account
models = client.models.list()

# Print them out
for m in models.data:
    print(m.id)
