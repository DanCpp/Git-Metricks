#!/usr/bin/env bash


mkdir -p ./test-data
touch ./test-data/data.json

curl -X 'GET' \
  'https://gateway-codemetrics.saas.sferaplatform.ru/app/sourcecode/api/api/v2/projects/public/repos/elastic/commits?cursor=&limit=&path=&fullHistory=true' \
  -H 'accept: application/json' \
  -H 'authorization: Basic ZGFuaWxhLnVzaGFrb3YuMDhAbWFpbC5ydTpHejdBRUhSQ2o5N2I=' > ./test-data/data.json