#!/bin/bash

# Define the API endpoint
API_URL="http://localhost:8000/submit"

# Define the dummy object as a JSON string
DUMMY_OBJECT='{
  "root": {
    "name": "root",
    "ast": {
        "key1": "value1",
        "key2": "value2"
    },
    "source": "source code"
  },
  "dependencies": [
    {
      "name": "dependency1",
      "ast": {
        "key1": "value1",
        "key2": "value2"
      },
      "source": "source code"
    },
    {
      "name": "dependency2",
      "ast": {
        "key1": "value1",
        "key2": "value2"
      },
      "source": "source code"
    }
  ]
}'

curl -X POST "$API_URL" \
     -H "Content-Type: application/json" \
     -d "$DUMMY_OBJECT"

echo
