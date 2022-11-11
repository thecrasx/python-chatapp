from server.errors import WorkDirNotValidError, ConfigPathNotValidError
import json
import os


CONFIG_DIR = ".\config"

class PathLoader:
    def __init__(self, key):
        self._key = key
        self._json_data = None

        PATH_JSON = CONFIG_DIR + "\path.json"
        FULL_PATH = os.getcwd() + CONFIG_DIR[1:] # "[1:]" removes the dot at the beginning

        if os.path.exists(PATH_JSON):
            
            with open(PATH_JSON, "r") as jf:
                self._json_data = json.load(jf)

            self._workdir = self._json_data["Working Directory"]

            if self._workdir != "./":
                
                # Update working directory
                if self._workdir != os.getcwd():
                    if os.path.exists(self._workdir):
                        os.chdir(self._workdir)

                    else:
                        raise WorkDirNotValidError(FULL_PATH, self._workdir)
        
        else:
            raise ConfigPathNotValidError(FULL_PATH)

    def getPath(self):
        return self._workdir + self._json_data["path"][self._key]

