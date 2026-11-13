import os

JOKE = "My coding agent billed me for 200,000 tokens to write 'Hello, World.' I asked for an itemized receipt. It sent a 400,000-token explanation of why the receipt cost extra."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
