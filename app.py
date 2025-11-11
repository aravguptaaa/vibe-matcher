# app.py

import streamlit as st
import pandas as pd
import ollama
from sklearn.metrics.pairwise import cosine_similarity

# --- Backend Logic (from your notebook) ---

# Use Streamlit's caching to load data and generate embeddings only once
@st.cache_data
def load_and_embed_data():
    """Loads product data and generates embeddings, then caches the result."""
    print("--- Running Initial Data Load and Embedding ---")
    data = {
        "name": ["Boho Maxi Dress", "Streetwear Hoodie", "Minimalist Blazer", "Vintage Leather Jacket", "Cozy Knit Sweater", "High-Top Sneakers"],
        "desc": ["Flowy, with earthy tones and floral patterns for a free-spirited look.", "Oversized fit, bold graphic print, and heavyweight cotton for city streets.", "A clean, tailored cut in a neutral tone for a sharp, professional look.", "Distressed authentic leather with a timeless, iconic biker silhouette.", "A soft, warm cable-knit pullover for relaxing evenings by the fire.", "Classic design with vibrant color accents. The perfect urban footwear."]
    }
    df = pd.DataFrame(data)
    
    embeddings = [
        ollama.embeddings(model='nomic-embed-text', prompt=desc)['embedding']
        for desc in df['desc']
    ]
    df['embeddings'] = embeddings
    print("--- Caching Complete ---")
    return df

def find_vibe_matches(query, df, top_n=3, score_threshold=0.6):
    """Finds the top N products matching the query vibe."""
    query_embedding = ollama.embeddings(model='nomic-embed-text', prompt=query)['embedding']
    product_embeddings = list(df['embeddings'])
    similarities = cosine_similarity([query_embedding], product_embeddings)[0]
    
    results_df = df.copy()
    results_df['score'] = similarities
    strong_matches = results_df[results_df['score'] >= score_threshold]
    
    if strong_matches.empty:
        return pd.DataFrame()

    return strong_matches.sort_values(by='score', ascending=False).head(top_n)

# --- Streamlit User Interface ---

st.title("🛍️ Vibe Matcher")
st.write("Describe a vibe, and I'll find the perfect products for you!")

# Load the data (will be cached after the first run)
products_df_with_embeddings = load_and_embed_data()

# User input text box
user_query = st.text_input("Enter a vibe (e.g., 'energetic urban chic')", "")

if user_query:
    with st.spinner('Finding your vibe...'):
        matches = find_vibe_matches(user_query, products_df_with_embeddings)

        if not matches.empty:
            st.header("Here are your top matches!")
            for _, row in matches.iterrows():
                st.subheader(row['name'])
                st.write(f"**Vibe Match Score:** {row['score']:.2f}")
                st.write(f"**Description:** {row['desc']}")
                st.divider()
        else:
            st.warning("Sorry, couldn't find a strong match for that vibe. Please try another!")
