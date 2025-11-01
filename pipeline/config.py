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
    Base_url = conf.get_url()
    Limit  = conf.get_limit()
    Timeout = conf.get_timeout()
    # print("URL:", Base_url)
    # print("Timeout:", Timeout)
    # print("Limit:", Limit)

print("URL:", Base_url)
print("Timeout:", Timeout)
print("Limit:", Limit)



