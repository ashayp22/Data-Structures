class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    '''
    First, we check the users in this group to see if our user is there
    '''
    for u in group.get_users():
        if u == user:
            return True
    '''
    If the user isn't found, we try each of the groups
    '''
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False

print(is_user_in_group(sub_child_user, parent))
#True
print(is_user_in_group(sub_child_user, child))
#True
print(is_user_in_group(sub_child_user, sub_child))
#True