import google.generativeai as genai
from settings import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def generate_response(context: str, query: str) -> str:
    """
    Generates a response using the Gemini model based on provided context and query.
    """
    # --- UPDATED PROMPT: USE CONTEXT FIRST, THEN LLM KNOWLEDGE IF NEEDED ---
    prompt = f"""
    You are 'TravelBot', an expert AI assistant for a travel agency. Your tone should be friendly, professional, and helpful.
    
    Instructions:
    1. If the provided "Context" contains information relevant to the user's query, use it in your answer.
    2. If the context does NOT contain relevant information, IGNORE the context and answer using your own general knowledge as an AI language model.
    3. Never say you don't have enough information unless you truly cannot answer, even with your own knowledge.
    4. If you use your own knowledge, you may say: "(Answer based on general knowledge)" at the start of your answer.
    
    Context:
    {context}
    
    ---
    
    User's Query:
    {query}
    
    Answer:
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean up the response to remove potential markdown and extra whitespace
        return response.text.strip()
    except Exception as e:
        print(f"An error occurred while generating response: {e}")
        return "Sorry, I'm having trouble generating a response right now. Please try again later."