import os
from dotenv import load_dotenv
class Config:
    DEBUG = False
    TESTING = False
    FILE_TYPE = os.getenv("FILE_TYPE", "pdf,image,docx")  # Default file types

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")


class ProductionConfig(Config):
    ENV = "production"

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ENV = "testing"
    
    
    
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

def reload_config():
    global config
    config = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
        "testing": TestingConfig,
    }
def load_env_variables():
    load_dotenv(dotenv_path=".env", verbose=True, override=True)
    env_name = os.getenv("FLASK_ENV", "development")
    return env_name