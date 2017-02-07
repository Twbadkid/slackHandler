# slackHandler
Handler for python logging module to send slack message


# How to install
pip install git+https://github.com/Twbadkid/slackHandler.git

# How to Use
```
import logging
from slackHandler import slackHandler
# target can be a channel or a user, like #general or @koibadkid
# optional: as_user, send message as custom bot info, instead of 'bot' user, bot should be invited into channel.
handler = slackHandler('Your-slack-api-token','target',as_user=True)
handler.setLevel(logging.DEBUG)
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG) 
logger.addHandler(handler)

'''
code...
'''
logger.warning('This is a warning')
```
