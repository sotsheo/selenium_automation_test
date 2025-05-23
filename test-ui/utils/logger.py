"""
Thiết lập logging cho test.
"""
import logging
import os
from .config import Config

def setup_logger():
    log_dir = Config.REPORT_DIR
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'test.log')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)s | %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()
