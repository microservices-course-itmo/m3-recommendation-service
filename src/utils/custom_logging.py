import logging
import os
import sys
import typing

import logstash


# Duplicate so we don't bind to Django settings in external module
LOGSTASH_URL: typing.Optional[str] = os.getenv('S_LOGSTASH_HOST', None)
if LOGSTASH_URL:
    LOGSTASH_HOST, _logstash_port_raw = LOGSTASH_URL.split(':')
    LOGSTASH_PORT = int(_logstash_port_raw)


class ServiceNameLoggingFilter(logging.Filter):
    def filter(self, record):
        record.serviceName = 'ml3-recommendation-service'
        return True


logger = logging.getLogger('exception')

stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

if LOGSTASH_URL:
    logstash_handler = logstash.TCPLogstashHandler(
        LOGSTASH_HOST,
        LOGSTASH_PORT,
        version=1,
    )
    logger.addHandler(logstash_handler)

logger.addFilter(ServiceNameLoggingFilter())


def log_unhandled_exception(exc_type, exc_value, exc_traceback):
    logger.error(
        f"Unhandled exception: {exc_type} ({exc_value})!",
        exc_info=(exc_type, exc_value, exc_traceback),
    )


sys.excepthook = log_unhandled_exception
