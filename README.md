This script can be use to send the salary slip in the the form of attachment (or any user specific attachment) to the N number of users to their asana tasks. This can reduce manual effort to send users salary slip.

Script needs **task_id_dict.txt** & **Attachment** in particular format

**task_id_dict.txt** => contains username:taskID combination which is used to compare username fetched by attachment file name.

**Attachment format**
<anything>_<anything>_<username>.txt -> used to fetch username to get particular taskID from task_id_dict.txt
