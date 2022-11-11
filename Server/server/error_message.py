


CONFIG_DIR = "ChatApp\config"
SERVER_CONFIG_PATH = CONFIG_DIR + "\server_config.json"


class ErrorMessage:
    
    # PathLoader Error Messages
    def WorkDirNotValid(self, path_to_work_dir, entered_path):
        msg1 = f"\n\nPathLoader Error: Directory \"{entered_path}\" does not exist\n"
        msg2 = f"You can change \"Working Directory\" in {CONFIG_DIR}\path.json\n"
        return msg1 + msg2


    def ConfigPathNotValid(self, entered_path):
        msg1 = f"\n\nPathLoader Error: Directory \"{entered_path}\" does not contain \"path.json\" file\n"
        msg2 = f"This file is originally located at: {CONFIG_DIR}\n"
        return msg1 + msg2

    

    # ServerConfig Error Message
    def ServerConfigPathNotValid(self, entered_path):
        msg1 = f"\n\nServerConfig Error: File \"server_config.json\" not found at \"{entered_path}\"\n"
        msg2 = f"You can change \"Server Configuration\" path in {CONFIG_DIR}\path.json\n"
        return msg1 + msg2


    def IPNotConfigured(self):
        msg1 = "\n\nServerConfig Error: IP is not configured\n"
        msg2 = f"You can configure it in {SERVER_CONFIG_PATH}\n"
        return msg1 + msg2


    def PORTNotConfigured(self):
        msg1 = "\n\nServerConfig Error: PORT is not configured\n"
        msg2 = f"You can configure it in {SERVER_CONFIG_PATH}\n"
        return msg1 + msg2