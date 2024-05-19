from admin import Admin

admin_nine = Admin('norawee', 'laohateerapong', 17, 'male')
print(admin_nine.describe_user())
admin_nine.privileges.show_privileges()