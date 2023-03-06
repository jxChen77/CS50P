# import sys
# import requests

# if len(sys.argv) != 2:
#     sys.exit()

# reponse = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
# print(reponse.json())

# import json
# import sys
# import requests

# if len(sys.argv) != 2:
#     sys.exit()

# reponse = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
# print(json.dumps(reponse.json(),indent=2))

# import json
# import sys
# import requests

# if len(sys.argv) != 2:
#     sys.exit()

# reponse = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+ sys.argv[1])
# o = reponse.json()
# for result in o["results"]:
#     print(result["trackName"])

import sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])