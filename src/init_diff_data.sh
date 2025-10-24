#!/usr/bin/env bash

curl -X 'GET' \
  "https://gateway-codemetrics.saas.sferaplatform.ru/app/sourcecode/api/api/v2/projects/public/repos/elastic/commits/$1/diff?binary=false" \
  -H 'accept: application/json' \
  -H 'authorization: Basic ZGFuaWxhLnVzaGFrb3YuMDhAbWFpbC5ydTpHejdBRUhSQ2o5N2I=' > ./test-data/data_$1.json