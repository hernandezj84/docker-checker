"""Tests for requests_helper"""

import os
from src.requests_helper import send_message

def test_send_message():
    """Tests send_message function"""
    result = send_message("this is a test from pytest")
    assert result.status_code == 200
    print(result)


