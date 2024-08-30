import requests
from datetime import datetime, timedelta

time = None
def get_last_accepted_problem(user_handle):
    url = f'https://codeforces.com/api/user.status?handle={user_handle}'

    response = requests.get(url)
    data = response.json()

    if data['status'] == 'OK':
        submissions = data['result']

        accepted_problems = [sub for sub in submissions if sub['verdict'] == 'OK']

        if accepted_problems:
            last_problem = accepted_problems[0]
            submission_time = last_problem['creationTimeSeconds']

            global time
            if not time == None:
                if time != submission_time:
                    return True
                else:
                    return False
            else:
                time = submission_time
        else:
            print("No accepted problems found.")
            exit(0)
    else:
        print("Failed to retrieve submissions.")
        exit(0)
