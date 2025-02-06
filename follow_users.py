"""
this is a script for following users back on instagram
"""
import os
import sys
from instagrapi import Client
from instagrapi.exceptions import (
    BadPassword, ReloginAttemptExceeded, ChallengeRequired,
    SelectContactPointRecoveryForm, RecaptchaChallengeForm,
    FeedbackRequired, PleaseWaitFewMinutes, LoginRequired
)

from dotenv import load_dotenv

load_dotenv()

def main():
    """
    authenticate with the api
    grab our followers
    iterate over follower, follow user
    """
    client = Client()
    ACCOUNT_USERNAME = os.getenv("IG_USERNAME")
    ACCOUNT_PASSWORD = os.getenv("IG_PASSWORD")
    
    login(cl=client, username=ACCOUNT_USERNAME, password=ACCOUNT_PASSWORD)

    followers = get_followers(cl=client)

    following = get_following(cl=client)

    for user_id, user in followers.items():
        if user_id not in following:
            follow_user(cl=client, user=user)

def login(cl: Client, username, password, attempts=1, max_retries=3):
    """
    login to instagram api client

    Args:
        cl (Client): api client

    Returns:
        bool: login successful
    """
    if attempts > max_retries:
        print("max retries exceeded, failed to authenticate with API.")
        raise ConnectionError

    try:
        print(f"authenticating with the API, attempt: {attempts}, max_retries: {max_retries}")
        if cl.login(username=username, password=password):
            return True
    except ChallengeRequired:
        # TODO: implement challenge resolution
        print("TODO: implement challenge resolution")
    except Exception as ex:
        print(type(ex))
        print(ex)
    finally:
        attempts += 1
        login(cl=cl, username=username, password=password, attempts=attempts)

def get_followers(cl: Client) -> dict:
    """
    get followers
    Args:
        cl (Client): api client
        user_id (int): user id
        
    Returns:
        bool: user followed
    """
    try:
        print("extracting followers")
        return cl.user_followers(user_id=cl.user_id)
    except Exception as ex:
        print(type(ex))
        print(ex)

def get_following(cl: Client) -> dict:
    """
    get users the client is following

    Args:
        cl (Client): _description_

    Returns:
        dict: _description_
    """
    try:
        print("extracting followed users")
        return cl.user_following(user_id=cl.user_id)
    except Exception as ex:
        print(type(ex))
        print(ex)

def follow_user(cl: Client, user: int) -> bool:
    """
    follow user
    Args:
        cl (Client): api client
        user_id (int): user id
        
    Returns:
        bool: user followed
    """
    try:
        print(f"Following user, {user.username}")
        return cl.user_follow(user_id=user.pk)
    except Exception as ex:
        print(type(ex))
        print(ex)

if __name__ == "__main__":
    main()