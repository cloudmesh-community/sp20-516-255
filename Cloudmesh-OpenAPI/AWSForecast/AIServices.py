class AIServices:

    def __init__(self, name='aws'):

        from cloudmesh.configuration.Config import Config

        self.conf = Config()["cloudmesh"]

        self.user = Config()["cloudmesh"]["profile"]["user"]
        self.spec = self.conf["cloud"][name]

        self.cloudname = name

        self.default = self.spec["default"]
        self.cloudtype = self.spec["cm"]["kind"]

        #Read the configuration file
        import configparser
        config = configparser.ConfigParser()
        config.sections()

        config.read('AITimeSeries.cfg')

        if (self.cloudname == 'aws'):
            print("AWS Cloud was requested")
        elif self.cloudname == 'Azure':
            print("Azure cloud was requested")
        else :
            print("Supported cloud services at this time : ")

