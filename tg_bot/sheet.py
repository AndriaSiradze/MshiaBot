import gspread

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
s_a = gspread.service_account('tg_bot/creds.json', scopes=scopes)

sheet = s_a.open("mshiabot").sheet1
hello = sheet.col_values(1)[-1]