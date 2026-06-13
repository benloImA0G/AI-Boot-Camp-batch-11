## ============================================================
## ResumeFit AI v5.0 — Colab Runner Cell
## ============================================================

# 1. Install dependencies FIRST (before any imports)
print("Installing dependencies...")
!pip -q install streamlit pypdf scikit-learn plotly openai pyngrok python-docx \
    pinecone sentence-transformers

# 2. Now import (packages are guaranteed to exist)
import os
import time
from pyngrok import ngrok
from google.colab import userdata

# 3. Load secrets
try:
    token = userdata.get('NGROK_AUTH_TOKEN').strip()
    ngrok.set_auth_token(token)
    os.environ["NGROK_AUTH_TOKEN"] = token
    print("NGROK_AUTH_TOKEN loaded ✅")
except Exception as e:
    print("❌ Error loading NGROK_AUTH_TOKEN."); raise e

try:
    groq_key = userdata.get('GROQ_API_KEY').strip()
    os.environ['GROQ_API_KEY'] = groq_key
    print("GROQ_API_KEY loaded ✅")
except:
    print("⚠️ GROQ_API_KEY not found — app will use rule-based mode.")

try:
    pinecone_key = userdata.get('PINECONE_API_KEY').strip()
    os.environ['PINECONE_API_KEY'] = pinecone_key
    print("PINECONE_API_KEY loaded ✅")
except:
    print("⚠️ PINECONE_API_KEY not found — semantic scoring will be skipped.")

# 4. Cleanup & restart
ngrok.kill()
!pkill streamlit

# 5. Run the Streamlit app
APP_FILE = "app.py"
if os.path.exists(APP_FILE):
    print(f"Starting {APP_FILE} ...")
    get_ipython().system_raw(f'streamlit run {APP_FILE} --server.port 8501 --server.address 0.0.0.0 &')
    time.sleep(6)
    try:
        tunnel = ngrok.connect(8501, "http")
        print("\n" + "="*60)
        print("🚀 ResumeFit AI v5.0 is live!")
        print(f"🔗 Public URL: {tunnel.public_url}")
        print("="*60)
        print()
        print("⏳ FIRST TIME LOADING NOTICE:")
        print("   The AI embedding model (all-MiniLM-L6-v2, ~80MB) is")
        print("   downloading in the background from HuggingFace.")
        print("   ➡ Please wait ~60 seconds before opening the URL.")
        print("   ➡ This only happens ONCE per session — next time is instant.")
        print("="*60)
    except Exception as e:
        print(f"\n❌ Ngrok error: {e}")
else:
    print(f"❌ '{APP_FILE}' not found. Run Cell 1 first.")
