import logging

audit_logger = logging.getLogger("audit")

def log_event(user, action, details=""):

    audit_logger.info(
        f"USER={user} ACTION={action} DETAILS={details}"
    )