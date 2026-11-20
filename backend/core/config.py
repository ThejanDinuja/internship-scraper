import os 
import dotenv

dotenv.load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
# print(DATABASE_URL)

# Authentication settings
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
AUTH0_AUDIENCE = os.getenv("AUTH0_AUDIENCE")