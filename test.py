from enum import Enum


class Config(Enum):
    PORT = 8080
    HOST = "STARWARS"
    USER = "PRASHANT"


breakpoint()
print(Config.PORT)
