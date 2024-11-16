This page talks about how to setup terraform for GCP.
Create a custom Service account for Terraform in IAM with Editor role.
After creation, go to manage keys for the SA and add key as json file.
Download the json file to local path.
Move the file to Terraform codebase folder and rename as credentials.json.

More info - https://youtu.be/e_8LZL2Th_4?list=PLpZQVidZ65jO_wtOpLv-HmC9uJgTRB8GT