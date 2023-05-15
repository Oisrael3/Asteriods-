from Comms import CommsListener, CommsSender
import sys
import json

class Messenger:
    def __init__(self, creds, callback=None):
        self.creds = creds
        self.callBack = callback

        if not self.creds:
            print(
                "Error: Message handler needs `creds` or credentials to log into rabbitmq. "
            )
            sys.exit()

        if self.callBack != None:
            # Start the comms listener to listen for incoming messages
            self.commsListener.threadedListen(self.callBack)

        self.user = self.creds["user"]

        # create instances of a comms listener and sender
        # to handle message passing.
        self.commsListener = CommsListener(**self.creds)
        self.commsSender = CommsSender(**self.creds)

    def send(self, target, body):
        """ """
        self.commsSender.send(
            target=target, sender=self.user, body=json.dumps(body), closeConnection=False
        )

    def setCallback(self, callBack):
        self.callBack = callBack
        self.commsListener.threadedListen(self.callBack)