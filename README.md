# Vibe Matcher 🛍️

An intelligent fashion recommendation engine that finds products based on a  *vibe* , not just keywords. This project uses local embedding models via Ollama and vector similarity search to provide a semantic, intuitive, and private-by-design search experience.
Live Demo: 

https://www.loom.com/share/dbe18fb588384adb9d6fcdb3c539c4e4

## ✨ Core Concept

Traditional search is limited to keyword matching. The Vibe Matcher understands the *semantic meaning* behind a user's query.

1. **User Input** : A user describes a feeling or style, like "energetic urban chic".
2. **Vectorization** : The user's query and all product descriptions are converted into numerical vectors (embeddings) using a local language model (Ollama).
3. **Similarity Search** : The system uses **Cosine Similarity** to mathematically find and rank the products whose "vibe vector" is closest to the query's vector.

## 🚀 Features

* **Semantic Search** : Go beyond keywords to understand user intent and feeling.
* **Local & Private** : Powered by  **Ollama** , no data is sent to external APIs. No API keys needed.
* **Interactive UI** : A simple and clean user interface built with  **Streamlit** .
* **Scalable Foundation** : The core logic is a prototype for large-scale production systems.

## 🛠️ Tech Stack

* **Backend** : Python
* **Web Framework** : Streamlit
* **LLM & Embeddings** : Ollama (nomic-embed-text model)
* **Data Manipulation** : Pandas
* **Vector Math** : Scikit-learn

## ⚙️ Setup and Installation

Follow these steps to get the Vibe Matcher running on your local machine.

### Prerequisites

* Python 3.8+
* [Ollama](https://ollama.com/) installed and running on your machine.

### Step-by-Step Guide

1. **Clone the repository:**
   <pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">bash</span></div></div><pre><code class="language-bash"><span class="token">git</span><span> clone https://github.com/your-username/vibe-matcher.git
   </span><span></span><span class="token">cd</span><span> vibe-matcher</span></code></pre></div></pre>
2. **Create and activate a virtual environment:**
   <pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">bash</span></div></div><pre><code class="language-bash"><span class="token"># Create the environment</span><span>
   </span>python3 -m venv venv

   <span></span><span class="token"># Activate it (on macOS/Linux)</span><span>
   </span><span></span><span class="token">source</span><span> venv/bin/activate</span></code></pre></div></pre>
3. **Install the required packages:**
   <pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">bash</span></div></div><pre><code class="language-bash"><span>pip </span><span class="token">install</span><span> -r requirements.txt</span></code></pre></div></pre>
4. **Download the embedding model via Ollama:**
   <pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">bash</span></div></div><pre><code class="language-bash"><span>ollama pull nomic-embed-text</span></code></pre></div></pre>

## ▶️ How to Run

1. Ensure the Ollama application is running in the background.
2. Run the Streamlit app from your terminal:
   <pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">bash</span></div></div><pre><code class="language-bash"><span>streamlit run app.py</span></code></pre></div></pre>
3. Open your web browser and navigate to the local URL provided by Streamlit (usually http://localhost:8501).

## 📁 Project Structure

<pre class="p-0 m-0 rounded-xl"><div class="rt-Box relative"><div class="rt-Flex rt-r-fd-column rt-r-py-1 rt-r-w absolute top-2 z-10 px-[14px]"><div class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-jc-space-between"><span data-accent-color="gray" class="rt-Text">text</span></div></div><pre><code class="language-text"><span>vibe-matcher/
</span>├── app.py              # The Streamlit web application
├── VibeMatcher.ipynb   # The original Jupyter Notebook prototype
├── requirements.txt    # Python package dependencies
└── README.md           # You are here!</code></pre></div></pre>

## 🔮 Future Vision & Improvements

This project serves as a powerful proof-of-concept. The next steps to productionize and enhance the system include:

* **Integrate a Vector Database** : Replace the current linear scan with a dedicated vector database like  **Pinecone** ,  **Weaviate** , or **Milvus** to enable real-time search across millions of products.
* **Fine-Tune the Embedding Model** : Fine-tune the embedding model on a fashion-specific dataset to teach it the nuanced vocabulary of the industry, improving match accuracy.
* **Implement Multi-Modal Search** : Extend the system to accept images as search queries. A user could upload a photo, and the system would find products with a similar visual vibe using models like CLIP.
