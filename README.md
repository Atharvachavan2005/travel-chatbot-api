# Travel Chatbot API

A simple AI-powered travel assistant for travel agencies. Users can ask travel-related questions and get instant answers from the agency's knowledge base or the AI's general knowledge. Includes a Streamlit frontend and FastAPI backend.

## Features
- Answers travel FAQs and trip details
- Uses your agency's knowledge base
- Streamlit web interface

## Technologies Used
- **Python**: Main programming language
- **FastAPI**: Backend API framework
- **Streamlit**: Frontend web app
- **Google Generative AI (Gemini)**: LLM for generating answers
- **ChromaDB**: Vector database for retrieval-augmented generation (RAG)
- **Sentence Transformers**: For text embeddings
- **Pandas**: Data handling and CSV processing

## Quick Start
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the backend:**
   ```bash
   uvicorn main:app --reload
   ```
3. **Run the frontend:**
   ```bash
   streamlit run frontend.py
   ```

## Description
TravelBot helps users get travel information, itineraries, and answers to common questions using both your data and AI expertise. 