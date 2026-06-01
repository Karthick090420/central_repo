from anthropic import Anthropic
import os

# Initialize Claude Client

client = Anthropic(
api_key=os.environ["CLAUDE_API_KEY"]
)

# Repository location

repo_path = "target_repo"

# Skill file path

skill_file = os.path.join(repo_path, "skill.md")

if not os.path.exists(skill_file):
raise Exception("skill.md not found in repository")

# Read skill instructions

with open(skill_file, "r", encoding="utf-8") as f:
skill_content = f.read()

repo_content = []

# Read repository files

for root, dirs, files in os.walk(repo_path):

```
# Ignore unnecessary folders
dirs[:] = [
    d for d in dirs
    if d not in [
        ".git",
        "node_modules",
        "venv",
        "dist",
        "build",
        "target",
        "__pycache__"
    ]
]

for file in files:

    # Skip skill file since it is already read
    if file == "skill.md":
        continue

    if file.endswith(
        (
            ".py",
            ".java",
            ".js",
            ".ts",
            ".yml",
            ".yaml",
            ".json",
            ".properties",
            ".md",
            ".txt"
        )
    ):

        file_path = os.path.join(root, file)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            repo_content.append(
                f"\n\nFILE: {file_path}\n"
                f"{content}\n"
            )

        except Exception as e:
            print(f"Skipping {file_path}: {e}")
```

# Build prompt

prompt = f"""
You are a technical documentation expert.

Follow the instructions provided in the skill file.

SKILL INSTRUCTIONS:

{skill_content}

Analyze the complete repository and generate documentation.

REPOSITORY CONTENTS:

{''.join(repo_content)}
"""

# Call Claude API

response = client.messages.create(
model="claude-sonnet-4-0",
max_tokens=4000,
messages=[
{
"role": "user",
"content": prompt
}
]
)

# Extract response

documentation = response.content[0].text

# Write documentation file

with open("AI_DOCUMENTATION.md", "w", encoding="utf-8") as f:
f.write(documentation)

print("AI_DOCUMENTATION.md generated successfully")
