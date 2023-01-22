#Me at the zoo @ Youtube
#https://www.youtube.com/watch?v=jNQXAC9IVRw

import sys, json
from youtube_transcript_api import YouTubeTranscriptApi

videoId = "jNQXAC9IVRw"
outputFileName = "result.json"



#Fetch the subtitles using the YoutubeTranscript API
subs = YouTubeTranscriptApi.get_transcript(videoId)

# Save the result to a JSON-file
f = open(outputFileName, "w")
f.write(json.dumps(subs, indent=4))
f.close()