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
  --data "username=..."

curl -X POST http://kong:8001/consumers/.../basic-auth \
    --data "username=..." \
    --data "password=.."

