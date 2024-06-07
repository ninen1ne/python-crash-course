# This program tell information about my self  in dictionary form.
# 22/3/2024

def build_profile(first, last, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('norawee', 'laohaterapong',
                             location='nonthaburi',
                             grade=11,
                             age=17)
print(user_profile)
