from langchain_core.tools import tool
from agent.llm import get_llm
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from config import GRAPH_FOLDER
import numpy as np

#Excel Analyze tool

@tool("analyze_excel", description="Analyze an excel or csv")
def analyze_excel(file_path:str,user_query: str):
    df = pd.read_csv(file_path)
    data = df.head(15)
    humidity_data = df["Humidity9am"].head(20)
    temperature_data = df["MinTemp"].head(20)


    if "humidity with simple comparision" in user_query.lower():
        plt.figure()
        df[["Humidity9am", "Humidity3pm"]].plot()
        plt.title("Humidity Comparison")
        plt.savefig(f"{GRAPH_FOLDER}humidity_graph.png")
        plt.close()
        
    elif "temperature with simple comparision" in user_query.lower():
        print("Entered in the temp comp")
        plt.figure()
        df[["MinTemp", "MaxTemp"]].plot()
        plt.title("Temperature Comparison")
        plt.savefig(f"{GRAPH_FOLDER}Temp_graph.png")
        plt.close()

    elif "humidity with vertical bar" in user_query.lower():
        plt.bar(range(len(humidity_data)), humidity_data)

        plt.xlabel("Index")
        plt.ylabel("Humidity9am")
        plt.title("Humidity at 9am (First 20 Records)")

        plt.xticks(range(len(humidity_data)))
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}humidity_vertical_bar.png")
        plt.close()

    elif "temperature with vertical bar" in user_query.lower():
        plt.bar(range(len(temperature_data)), temperature_data)

        plt.xlabel("Index")
        plt.ylabel("MinTemp")
        plt.title("MinTemp of First 20 Records")

        plt.xticks(range(len(temperature_data)))
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}temp_vertical_bar.png")
        plt.close()

    elif "humidity with vertical comparison" in user_query.lower():
        df = pd.read_csv(file_path).head(15)
        x = np.arange(len(df))
        width = 0.5

        plt.figure()
        plt.bar(x-width/2, df["Humidity9am"], width)
        plt.bar(x+width/2, df["Humidity3pm"], width)

        plt.xlabel("Index")
        plt.ylabel("Humidity")
        plt.title("Humidity 9am vs 3pm")

        plt.xticks(x)
        plt.legend()
        plt.grid(axis="y")
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}humidity_vertical_comp_bar.png")
        plt.close()

    elif "temperature with vertical comparison" in user_query.lower():
        df = pd.read_csv(file_path).head(15)
        x= np.arange(len(df))
        width = 0.5

        plt.figure()
        plt.bar(x-width/2,df["MinTemp"], width)
        plt.bar(x+width/2,df["MaxTemp"], width)

        #plt.bar(range(len(humidity_data)), temperature_data)

        plt.xlabel("Index")
        plt.ylabel("Temperature")
        plt.title("MinTemp vs MaxTemp")

        plt.xticks(x)
        plt.tight_layout()
        plt.savefig(f"{GRAPH_FOLDER}temp_vertical_comparison_bar.png")
        plt.close()

    context = df.head(20).to_string()
    #summary = df.describe().to_string()

    llm = get_llm()

    report_prompt = f"""
    You are a data analyst.
    User request: {user_query}

    Dataset preview:
    {context}

    Generate a customized report based on user request.
    """
    return llm.invoke(report_prompt)