"""The upload command."""

from .base import Base
from bonita.api.bonita_client import BonitaClient


class Upload(Base):
    """Manage uploads"""

    def run(self):
        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
        self.bonita_client = BonitaClient(self.loadConfiguration())
        if self.options['upload']:
            self.upload()

    def upload(self):
        uploadType = self.options['<type>']
        filename = self.options['<filename>']
        rc, datas = self.bonita_client.upload(uploadType, filename)
        if rc == 200:
            print('OK')
            print('', datas)
        else:
            print('KO - %d' % rc)