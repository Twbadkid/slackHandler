import logging
from slacker import Slacker
class slackHandler(logging.Handler):
    def __init__(self,slack_api_token,target,as_user=False):
        super(self.__class__, self).__init__()
        self.slack = Slacker(slack_api_token)
        self.as_user = as_user
        self.target=target
    def emit(self, record):
        msg = self.format(record)
        self.slack.chat.post_message(self.target, msg,as_user=self.as_user)
