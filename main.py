# Before running this script, start the API server:
#
# > bin\headless.exe --port=1234

import json
import requests

api = 'http://localhost:1234'
hours_to_sim = '12:00:00'

def main():
    # Make sure to start the simulation from the beginning
    print('Did you just start the simulation? Time is currently',
          requests.get(api + '/sim/get-time').text)

if __name__ == '__main__':
    main()
