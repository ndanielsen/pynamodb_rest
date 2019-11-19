import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def http_response(body, status_code=200):
    if not isinstance(body, dict):
        body = dict(body)
    return build_response(status_code, body)


def build_response(status_code, body):
    logger.info(body)
    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
        "body": json.dumps(body),
    }

