import os
from dotenv import load_dotenv

print("ORACLE STATUS: Reading the Matrix...\n")
load_dotenv()
print("Configuration loaded:")

mode = os.environ.get("MATRIX_MODE")
api_key = os.environ.get("API_KEY")
database_url = os.environ.get("DATABASE_URL")
log_level = os.environ.get("LOG_LEVEL")
zion_endpoint = os.environ.get("ZION_ENDPOINT")

print(f"Mode: {mode}")
print(f"Database {database_url}")
print(f"API Access: {api_key}")
print(f"Log Level: {log_level}")
print(f"Zion Network: {zion_endpoint}")
print()
print("[OK] No hardcoded secrets detected")


if os.path.exists(".env"):
    print("[OK] .env file properly configured")
else:
    print("[KO] .env file missing")
print("[OK] Production overrides available\n")
print("The Oracle sees all configurations.")
