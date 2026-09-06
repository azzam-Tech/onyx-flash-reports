import os
from dotenv import load_dotenv

# Load environment variables before importing anything else
load_dotenv()

from waitress import serve
from app import create_app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    print(f"Starting ZATCA Printer Server on port {port} using Waitress...")
    
    app = create_app()
    serve(app, host="0.0.0.0", port=port, threads=8)
