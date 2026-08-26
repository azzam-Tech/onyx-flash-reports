import os
from dotenv import load_dotenv
from waitress import serve
from app import app

if __name__ == "__main__":
    load_dotenv()
    port = int(os.getenv("PORT", 8080))
    print(f"Starting ZATCA Printer Server on port {port} using Waitress...")
    serve(app, host="0.0.0.0", port=port, threads=8)
