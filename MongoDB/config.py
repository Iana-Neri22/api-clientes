import os


class Config:
    @staticmethod
    def load_env_variables(file_path=".env"):
        with open(file_path) as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"): 
                    key, value = line.split("=", 1)
                    os.environ[key] = value.strip().strip("'\"") 

