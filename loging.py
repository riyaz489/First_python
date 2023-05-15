import logging

logging.warning('you have been warned')
logging.critical('Abort Abort')
logging.info('info message')

#info will not print becoz logging level is set to warning
# to only warning and higher priority will get printed

# setting logging level
logging.root.setLevel(logging.INFO)
# ---or----
logging.basicConfig(level=logging.INFO)
# now info messages will get printed


# getting current logging level
logging.root.getEffectiveLevel()

# we can create wrapper for this logger which contains tag(), which will add key-value pair to each log line.
# this will be later helpful to use these tags as filters in kibana



