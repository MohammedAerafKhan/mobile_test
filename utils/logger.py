import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def get_logger(name: str = "TestLogger"):
    """
    Returns a configured logger instance.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:  # Prevent duplicate handlers
        logger.setLevel(logging.DEBUG)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File handler (logs/debug.log)
        file_handler = logging.FileHandler("logs/test_execution.log", mode="w")
        file_handler.setLevel(logging.DEBUG)

        # Format
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
