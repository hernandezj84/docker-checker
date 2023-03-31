"""Requests module"""

import requests
import os

SLACK_URL=os.getenv('SLACK_URL')

def send_message(message):
    """Send message to slack"""
    data = {"text": message}
    post = requests.post(url=SLACK_URL, json=data)
    return post
