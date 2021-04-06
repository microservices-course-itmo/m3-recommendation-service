import logging


class ServiceNameLoggingFilter(logging.Filter):
    def filter(self, record):
        record.serviceName = 'ml3-recommendation-service'
        return True
