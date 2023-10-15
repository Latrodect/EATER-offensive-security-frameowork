import logging

class CustomLogger:
    def __init__(self, log_file, log_level=1):
        self.logger = logging.getLogger(__name__)
        
        if log_level == 0:
            self.logger.setLevel(logging.DEBUG)
        elif log_level == 1:
            self.logger.setLevel(logging.INFO)
        elif log_level == 2:
            self.logger.setLevel(logging.ERROR)
        elif log_level == 3:
            self.logger.setLevel(logging.CRITICAL)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger