"""Tests for docker"""

from src.docker import is_docker_running

def test_is_docker_running():
    """Tests is_docker_running"""
    state = is_docker_running('wonderful_archimedes')
    print(state)
