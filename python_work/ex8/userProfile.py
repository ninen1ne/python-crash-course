# 7/5/2024
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    # Create newe dict because if I use user_info dict fname and lname will stored at the end of dict.
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('norawee','laohateerapong',
                             age=17,
                             location='nonthaburi')
print(user_profile)