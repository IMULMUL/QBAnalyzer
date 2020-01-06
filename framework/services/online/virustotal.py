from requests import get
from ...logger.logger import verbose, verbose_flag, verbose_timeout
from json import load,dumps

class VirusTotal:
    @verbose(True,verbose_flag,verbose_timeout,"Starting VirusTotal module")
    def __init__(self,tokens_path):
        with open(tokens_path,"r") as f:
            tokens = load(f)
            self.api = tokens["virustotal_key"]
            self.link = "https://www.virustotal.com/vtapi/v2"

    @verbose(True,verbose_flag,5,"Getting hash details from VirusTotal")
    def get_hash_details(self,hash) -> dict:
        parameters = {'resource': hash, 'apikey': self.api}
        return dumps(get("{}/file/report".format(self.link),params=parameters).json(),indent=4)

#print(virustotal().get_hash_details("63c29e8b364b208c806e8687c57c82f4ca10c359"))