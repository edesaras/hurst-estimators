from dotenv import load_dotenv
import os

load_dotenv()

os.system("poetry publish --build")
