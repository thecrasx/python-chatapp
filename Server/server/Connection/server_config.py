from socket import gethostbyname, gethostname
import json
import os

from server.errors import ServerConfigPathNotValidError, IPNotConfiguredError, PORTNotConfiguredError
from server.path_loader import PathLoader


class ServerConfig:
    def __init__(self):
        config_path = PathLoader("Server Configuration").getPath()
        
        if os.path.exists(config_path):       
            with open(config_path, "r") as f:
                data = json.load(f)
                config = data["Server Configuration"]

                self.IP = config["IP"]
                self.PORT = config["PORT"]
                
                if self.IP == "localhost":
                    self.IP = gethostbyname(gethostname())           
        else:
            raise ServerConfigPathNotValidError(config_path)

    def get(self): 
        if self.IP and self.PORT:
            return (self.IP, self.PORT)
        
        elif not self.IP:
            raise IPNotConfiguredError()

        elif not self.PORT:
            raise PORTNotConfiguredError()
            