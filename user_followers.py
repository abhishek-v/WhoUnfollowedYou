#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
import pickle

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


if __name__ == "__main__":

    ##
    ## WARNING: IF SHARING THE CODE, REMEMBER TO REMOVE YOUR PASSWORD HERE
    ##
    api = InstagramAPI("_abhishekvasudevan", "PASSWORD_GOES_HERE")
    api.login()

    user_id = api.username_id

    # List of all followers
    followers = getTotalFollowers(api, user_id)
    print('Number of followers:', len(followers))

    # Compare old and new followers list
    old = []
    updated = []
    new_id_map = {}
    old_id_map = {}

    ## Uncomment this block only when running for first time
    ## BEGIN BLOCK
    # for follower in followers:
    #     updated.append(follower['pk'])
    #     old_id_map[follower['pk']] = follower['username']
    # f = open("followers.pkl","wb")
    # pickle.dump(followers,f)
    # pickle.dump(old_id_map, f)
    # f.close()
    # updated = []
    ## END BLOCK

    f = open("followers.pkl","rb")
    old_list = pickle.load(f)
    old_id_map = pickle.load(f)

    for follower in old_list:
        old.append(follower['pk'])
    for follower in followers:
        updated.append(follower['pk'])

        # Add mapping of userId -> username
        new_id_map[follower['pk']] = follower['username']

    print("People who unfollowed you:")
    new_list = list(set(old)-set(updated))
    for unfollower in new_list:
        print(old_id_map[unfollower])

    # Save new followers list into the pickle file
    f = open("followers.pkl","wb")
    pickle.dump(followers,f)
    pickle.dump(old_id_map, f)

    f.close()
