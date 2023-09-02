import os
import json
import vertexai
from langchain.llms import VertexAI
# from google.cloud import secretmanager

def load_constants_locally():
    with open('constants.json', 'r') as f:
        data = json.load(f)
        
    global PROJECT_ID, MODEL_NAME, MAX_OUTPUT_TOKENS, TEMPERATURE, TOP_P, TOP_K, REGION
    PROJECT_ID = data["PROJECT_ID"]
    MODEL_NAME = data["MODEL_NAME"]
    MAX_OUTPUT_TOKENS = data["MAX_OUTPUT_TOKENS"]
    TEMPERATURE = data["TEMPERATURE"]
    TOP_P = data["TOP_P"]
    TOP_K = data["TOP_K"]
    REGION = data["REGION"]

def initialize_llm():
    load_constants_locally()
    
    # Initialize VertexAI and set up the LLM
    init_vertexai()
    return set_up_llm()

def init_vertexai():
    # Initialize VertexAI with the proper settings
    vertexai.init(project=PROJECT_ID, location=REGION)

def set_up_llm():
    # Set up the VertexAI with the specified parameters
    return VertexAI(
        model_name=MODEL_NAME,
        max_output_tokens=MAX_OUTPUT_TOKENS,
        temperature=TEMPERATURE,
        top_p=TOP_P,
        top_k=TOP_K,
        verbose=True,
    )