import logging
import os
from logging import config

from core.utils.utils import get_local_time

str_level_dict = {
    'info': logging.INFO,
    'debug': logging.DEBUG,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'critical': logging.CRITICAL
}


def init_logger(log_level, result_root, classifier, backbone):
    if log_level not in str_level_dict:
        raise KeyError

    level = str_level_dict[log_level]
    file_name = '{}-{}-{}.log'.format(classifier, backbone, get_local_time())
    log_path = os.path.join(result_root, file_name)

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'simple': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': level,
                'class': 'logging.StreamHandler',
                "formatter": "simple",
                "stream": "ext://sys.stdout"
            },
            'file': {
                'level': level,
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'simple',
                'filename': log_path,
                'maxBytes': 100 * 1024 * 1024,
                'backupCount': 3
            }
        },
        'loggers': {
            '': {
                'handlers': ['console', 'file'],
                'level': level,
                'propagate': True
            }
        }
    })