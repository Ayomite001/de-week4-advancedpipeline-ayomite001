from configparser import ConfigParser

class ConfigManager:
    def __init__(self, config_file = "pipeline.cfg"):
        self.config = ConfigParser()
        self.config.read(config_file ) 
    

    def get_url(self):
        return self.config.get("api", "base_url")
    
    def get_timeout(self):
        return self.config.getint("api", "timeout")
    
    def get_limit(self):
        return self.config.getint("api", "limit")
    
conf = ConfigManager()
    
if __name__ == "__main__":
    base_url = conf.get_url()
    limit  = conf.get_limit()
    timeout = conf.get_timeout()
    
# print("URL:", base_url)
# print("Timeout:", timeout)
# print("Limit:", limit)



