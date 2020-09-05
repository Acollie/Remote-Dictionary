# Remote Dictionary
## Simple flask based key value database.

### API
- `/get/<key>` this returns the value
- `/delete/<key>` this will remove the key and the associated value from the database
- `/add/<key>/<value>` this will add `key` as the key to the database and `value` as the value for that key.
- `/auth` This is the with the applications valid token (in the header `token`) will return a client access token

###