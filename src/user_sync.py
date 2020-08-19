
import requests
import os
from utils import *

def fetch_org_member(org_id):
    """Fetch user's login usernames from a GitHub org.

    Given a GitHub org name, this function will send a request to 
    fetch all members' login usernames from the given GitHub org.

    Args:
      org_id: str, the name of the GitHub org.

    Returns:
      A list of str. The list of user's login username.

    Raises:
      APIError: If the GitHub url returns a status code that is not 200.
    """
    org_url = "https://api.github.com/orgs/" + org_id + "/members"
    response = requests.get(org_url)
    if response.status_code != 200:
        raise APIError('GET /orgs/{}/members {}'.format(org_id, response.status_code))
    content = response.json()
    user_login_list = []
    for user in content:
        user_login_list.append(user['login'])
    return user_login_list


def fetch_user_public_key(user_login_id):
    """Given user login id, fetch user's public key.

    Args:
      user_login_id: str, user's login username.

    Returns:
      A list of str. The list of user's public keys.

    Raises:
      APIError: If the GitHub url returns a status code that is not 200.
    """
    url = "https://api.github.com/users/" + user_login_id + "/keys"
    response = requests.get(url)
    if response.status_code != 200:
        raise APIError('GET /users/{}/keys {}'.format(user_login_id, response.status_code))
    content = response.json()
    user_key_list = []
    for user in content:
        user_key_list.append(user['key'])
    return user_key_list
