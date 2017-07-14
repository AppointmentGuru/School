curl -i -X POST \
  --url http://kong:8001/apis/ \
  --data 'name=kong-admin' \
  --data 'uris=/manage' \
  --data 'strip_uri=true' \
  --data 'upstream_url=http://kong:8001'

curl -i -X POST \
  --url http://kong:8001/apis/kong-admin/plugins/ \
  --data 'name=basic-auth'

curl -i -X POST \
  --url http://kong:8001/consumers/ \
  --data "username=appointmentguru"

# curl -i -X POST \
#   --url http://kong:8001/consumers/$KONG_ADMIN_USER_NAME/key-auth/ \
#   --data 'key=4f6ae149-a6e1-45b7-8abc-dbf87f22e90b'

curl -X POST http://kong:8001/consumers/appointmentguru/basic-auth \
    --data "username=appointmentguru" \
    --data "password=4f6ae149-a6e1-45b7-8abc-dbf87f22e90b"
