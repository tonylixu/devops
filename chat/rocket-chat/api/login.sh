curl http://rocketchat:3000/api/v1/login -d "username=jarvis&password=password"
curl -H "X-Auth-Token: " -H "X-User-Id: " -H "Content-type: application/json" http://rocketchat:3000/api/v1/groups.create -d '{ "name": "testing" }'
curl -H "X-Auth-Token: " \
     -H "X-User-Id: " \
     -H "Content-type:application/json" \
     http://rocketchat:3000/api/v1/users.create \
     -d '{"name": "name", "email": "email@user.tld", "password": "anypassyouwant", "username": "uniqueusername", "customFields": { "twitter": "@userstwitter" } }'