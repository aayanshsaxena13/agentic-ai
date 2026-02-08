# Import the required library...
import pandas as pd
import os
import json

# Make the helper...
output_path = os.path.join(os.path.dirname(__file__), "..", "output", "chart.png")
input_path = os.path.join(os.path.dirname(__file__), "..", "input", "chart_info.json")

def createChart(title, kind, x, y, labels):
    with open(input_path, "r") as f:
        file = json.loads(f.read())
    
    df = pd.DataFrame(file)
    ax = df.plot(x=x, y=y, kind=kind, title=title, labels=file[labels])
    ax.get_figure().savefig(output_path, dpi=300)
    return "Generated graph using Agentic AI..."