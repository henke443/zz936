from util import logger_setup, log

logger = logger_setup("info", "./config.yaml", "mytemplate")
log("Hello")
