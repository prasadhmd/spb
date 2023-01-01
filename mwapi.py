#import logging
#logging.basicConfig(level = logging.INFO)
import json
import requests
from urllib import request

def connect_mw_dictionary(api_key, word):
  URL = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+word+"?key="+api_key
  PARAMS = {'word': word,'key': api_key}
  r = requests.get(url = URL, params = PARAMS)
  r.encoding = 'utf-8'
  if r.status_code == 200:
    return True, r.json()
  return False


api_key = "67027fd2-3477-4ca8-8f09-76b0b81bdd5c" # replace with you api key

words = open("3b.txt", "r").readlines()
f = open('3b_audio.txt', 'w')
fdef = open('3b_def.txt', 'w')
idx = 1
for word in words:
  hasaudio = 0
  fdef.write(str(idx) + '\n')
  status, result = connect_mw_dictionary(api_key, word)
  if status == True:
    try:
      base = result[0]['hwi']['prs'][0]['sound']['audio']
      if base.startswith('bix'):
        subdir = 'bix'
      else:
        if base.startswith('gg'):
          subdir = 'gg'
        else:
          subdir = base[0]
      audio_url = 'https://media.merriam-webster.com/audio/prons/en/us/mp3/' + subdir + '/' + base + '.mp3'
      response = request.urlretrieve(audio_url, '3b/' + str(idx) + ".mp3")
      hasaudio = 1

      for r in result:
        wdef = r['def'][0]['sseq'][0][0][1]['dt'][0][1]
        fdef.write(wdef + '\n')
    except:
      pass
  fdef.write('\n')
  if hasaudio == 0:
    f.write(word)
  idx = idx + 1

f.close()
fdef.close()
