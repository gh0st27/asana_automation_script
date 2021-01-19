##Main objective is to automate the process of sending the bulk attachment to the respective task ID

This script can be use to send the salary slip in the the form of attachment (or any user specific attachment) to the N number of users to their asana tasks. This can reduce manual effort to send users salary slip.

Script needs **task_id_dict.txt** & **Attachment** in particular format

**task_id_dict.txt** => contains username:taskID combination which is used to compare username fetched by attachment file name. (It will maintain the mapping of userID & taskID)

**Attachment format**

random_random_username.extension -> used to fetch username to get particular taskID from task_id_dict.txt (look attachment section)
