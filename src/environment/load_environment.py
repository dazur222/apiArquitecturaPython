from dotenv import dotenv_values
import os

def load_environment():
   environment = os.getenv("ENVIRONMENT") 
   env_file = f".env.{environment}"