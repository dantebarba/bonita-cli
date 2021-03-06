# -*- coding: utf-8 -*-
"""The session command."""

import json
from .base import Base
from bonita.api.bonita_client import BonitaClient


class Session(Base):
    """Manage sessions"""

    def run(self):
        #print('You supplied the following options:', json.dumps(self.options, indent=2, sort_keys=True))
        self.bonita_client = BonitaClient(self.loadConfiguration())
        if self.hasOption('login'):
            self.login()
        elif self.hasOption('logout'):
            self.logout()
        elif self.hasOption('get'):
            self.get()
        else:
            print("Nothing to do.")

    def login(self):
        url = self.options['<url>']
        username = self.options['<username>']
        password = self.options['<password>']

        rc = self.bonita_client.login(url, username, password)

        if rc == 200:
            self.saveConfiguration(self.bonita_client.getConfiguration())
        self.processResultCode(rc)

    def logout(self):
        rc = self.bonita_client.logout()
        self.processResultCode(rc)

    def get(self):
        rc, datas = self.bonita_client.getSession()
        self.processResults(rc, datas)
