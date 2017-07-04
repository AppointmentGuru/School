curl -i -X POST \
  --url http://kong:8001/apis/ \
  --data 'name=kong-admin' \
  --data 'uris=/manage' \
  --data 'strip_uri=true' \
  --data 'upstream_url=http://kong:8001'

curl -i -X POST \
  --url http://kong:8001/apis/kong-admin/plugins/ \
  --data 'name=key-auth'

curl -i -X POST \
  --url http://kong:8001/consumers/ \
  --data "username=$KONG_ADMIN_USER_NAME"

curl -i -X POST \
  --url http://kong:8001/consumers/admin/key-auth/ \
  --data 'key=$KONG_ADMIN_USER_TOKEN'

curl -i -X GET \
  --url http://165.227.141.208/manage/apis/ \
  --header "apikey: $KONG_ADMIN_USER_TOKEN"

