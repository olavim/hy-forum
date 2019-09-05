# Forum

> The Internet message board

A database application made as a part of practical work assignment.

# Description

A slightly modified version of the example topic "Keskustelufoorumi".

Users can post new messages inside message threads. Users are also allowed to edit and delete their own messages. Users can make new threads, and are allowed to change the title of their own threads later. Users are not allowed to delete threads; their own or anyone else's.

Users may search for threads inside a topic by their title, creation date, and name of the creator. Users may also search for individual messages inside a topic or thread by the date of posting, and name of the poster.

By default, users are shown all threads from newest to oldest, albeit paginated. Each thread is accompanied with information about: original poster, number of messages in thread, date of original post, date of latest post, name of the user who posted the latest message. The user will also see an indicator if the thread contains new messages since he/she previously opened it.

Users will need to identify themselves through a login portal. This identity is then connected to messages and threads a user creates, which is visible to all users.

The system includes permission groups, which affect how members of said groups can use the system. Members of a moderator group, for example, are allowed to edit and delete messages of other users. Members of admin group are allowed to create new permission groups, and change the members of a group.

Actions (assuming admin privileges):
- Login/Logout
- Create, edit, delete topic
- Create, edit, delete thread
- Create, edit, delete message
- List topics
- List and search threads in a topic
- List messages in a thread
- Search messages
- View, edit user details
- Create, edit, delete permission groups
- Add user to permission group

# Documents

- [Database relation diagram](documentation/db-chart.png)