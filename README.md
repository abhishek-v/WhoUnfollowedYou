# WhoUnfollowedYou
## What?
- Provides a python script which can be used to find out who unfollowed you on Instagram.
- The script has to be run manually every time you wish to see who unfollowed you.
- The script creates a pickle when it is first executed. For every subsequent execution, the script compares the old followers list with the new one retrieved from Instagram and determines who unfollowed you.
- The script makes use of the ```user_id``` field (this is the primary key used by Instagram and not the username for obvious reasons) returned for each follower for the comparison between old and new follower list. Therefore, even if someone changes their username, the script is unaffected.
- If someone has deactivated their account, their username will show up in the results as they are no longer in your new followers list.

## How to run this?
- Ensure you have python3 and pip installed.
- Install the InstagramAPI:
  ```pip3 install InstagramAPI```
- Add your username and password on line 37 (WARNING: Make sure you default this value back if you are going to share the script with anyone)
- Execute the script: ```python3 user_followers.py``` (Note that on the initial run, the unfollowers list will be empty)
- Uncomment the block of code on lines 54-61 for the initial run. This creates a pickle file which will be used for comparisons on subsequent runs.
- For subsequent runs, ensure the block of code on lines 50-57 is commented out.
