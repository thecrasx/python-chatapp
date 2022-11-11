from server.error_message import ErrorMessage

ErrorMsg = ErrorMessage()


class Error(Exception):
    pass

# PathLoader Errors
class WorkDirNotValidError(Error):
    def __init__(self, path_to_work_dir, entered_path):
        message = ErrorMsg.WorkDirNotValid(path_to_work_dir, entered_path)
        super().__init__(message)


class ConfigPathNotValidError(Error):
    def __init__(self, entered_path):
        message = ErrorMsg.ConfigPathNotValid(entered_path)
        super().__init__(message)


# ServerConfig Errors
class ServerConfigPathNotValidError(Error):
    def __init__(self, entered_path):
        message = ErrorMsg.ServerConfigPathNotValid(entered_path)
        super().__init__(message)


class IPNotConfiguredError(Error):
    def __init__(self):
        message = ErrorMsg.IPNotConfigured()
        super().__init__(message)


class PORTNotConfiguredError(Error):
    def __init__(self):
        message = ErrorMsg.PORTNotConfigured()
        super().__init__(message)



# Request Errors
class BadRequestError(Error):
    def __init__(self):
        pass