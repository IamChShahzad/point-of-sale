import os
from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

TPN = os.getenv("TPN")
AUTH_KEY = os.getenv("AUTH_KEY")
CARD_PERCENTAGE = float(os.getenv("CARD_PERCENTAGE",0)) 
# print(os.getenv("TPN"))
# print(os.getenv("AUTH_KEY"))