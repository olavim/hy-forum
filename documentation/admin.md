# User roles and permissions

The system includes a default administrator user whose roles and permissions cannot be changed, even by the administrator itself. This ensures that one cannot lock themself out of the system.

The username of said administrator user is `admin`, while the password depends on configuration.

The administrator is not the only user who can modify the roles and permissions of other users, however. Every permission the administrator has can be granted to other users.

To access the management page, navigate to `/admin`, or click the **admin**-link in the top left corner. The management page can only be accessed by a user with sufficient privileges, such as the administrator.

## User management

In this page is listed all the registered users. As you can see, the `admin` user is also listed, although you cannot edit its roles. To edit a user's roles, click the edit/pencil button on the right side of each user. If the list is empty (apart from the admin user), you may register a test user for the sake of this guide.

Unless you have already created roles, you will notice that the selected user has no roles, and you cannot add any either. Take a look at the *role management* section to find out how to create some.

Users may have multiple roles. This allows you to better group permissions together into roles other than just "moderator" and "administrator".

## Role management

In this page is listed all the roles that exist in the system. Unless you have already created roles, this list will be empty. Click the **New Role** button to create a new role. Give the role a name and save it.

After creating a role, you may assign *permissions* to it. If, for example, you add the `messages:edit` permission to the role, then any user with this role may edit messages of any user.

The role you created is now selectable in the user management section.

**Note:** You may give other users access to the management panel by giving them a role with the `roles:manage` permission.