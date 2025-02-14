import gspread
from google.oauth2.service_account import Credentials

# Google Sheets API Configuration
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "client_secret.json"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)

SHEET_ID = "e7152f0d7c3a1bbe/EfBgQL5YwLtEjtpdh9zpMocBvb6OCdE9zokhfoObC5RCcg?e=QIRZxE"
SHEET_NAME = "Form Responses"

def get_submitted_users():
    sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    submitted_users = [row["Email"] for row in data if row["Email"]]
    return submitted_users
