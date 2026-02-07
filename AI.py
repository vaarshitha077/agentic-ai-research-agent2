2. agent.py (Main Agent Controller)

```python
from tools import search_papers, summarize_paper, store_output
from memory import AgentMemory

def agentic_ai(goal):
    memory = AgentMemory()
    
    print("Goal received:", goal)
    
    # Step 1: Search
    papers = search_papers("AI in agriculture 2023 2024")
    top_papers = papers[:3]
    memory.store("papers", top_papers)
    
    # Step 2: Summarize
    summaries = []
    for paper in top_papers:
        summary = summarize_paper(paper)
        summaries.append(summary)
    
    memory.store("summaries", summaries)
    
    # Step 3: Store Output
    store_output(summaries)
    print("Task completed successfully.")

if __name__ == "__main__":
    agentic_ai(
        "Find the top 3 recent AI research papers on agriculture and summarize them"
    )
🔹 3. tools.py (Agent Tools)
def search_papers(query):
    # Simulated research papers
    return [
        {
            "title": "AI-Based Crop Yield Prediction",
            "year": 2024
        },
        {
            "title": "Computer Vision in Precision Agriculture",
            "year": 2024
        },
        {
            "title": "Reinforcement Learning for Smart Irrigation",
            "year": 2023
        }
    ]

def summarize_paper(paper):
    return {
        "title": paper["title"],
        "year": paper["year"],
        "summary": "This paper explores AI techniques to improve agricultural productivity."
    }

def store_output(data):
    import json
    with open("output/sample_output.json", "w") as f:
        json.dump(data, f, indent=4)
🔹 4. memory.py (Context / Memory Handling)
class AgentMemory:
    def __init__(self):
        self.memory = {}

    def store(self, key, value):
        self.memory[key] = value

    def retrieve(self, key):
        return self.memory.get(key)
🔹 5. sample_output.json (Expected Output)
[
    {
        "title": "AI-Based Crop Yield Prediction",
        "year": 2024,
        "summary": "This paper explores AI techniques to improve agricultural productivity."
    },
    {
        "title": "Computer Vision in Precision Agriculture",
        "year": 2024,
        "summary": "This paper explores AI techniques to improve agricultural productivity."
    },
    {
        "title": "Reinforcement Learning for Smart Irrigation",
        "year": 2023,
        "summary": "This paper explores AI techniques to improve agricultural productivity."
    }
]
🔹 6. requirements.txt
python>=3.8
