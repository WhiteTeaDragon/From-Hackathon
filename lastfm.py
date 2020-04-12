import pylast

# You have to have your own unique two values for API_KEY and API_SECRET
# Obtain yours from https://www.last.fm/api/account/create for Last.fm
API_KEY = "70d48262b0e787315b7cce695159b899"  # this is a sample key
API_SECRET = "5150bc25a89cc30e9f7454e12a3afbac"

# In order to perform a write operation you need to authenticate yourself
username = "AlexSend57"
password_hash = pylast.md5("0nly4YOU!")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash, session_key=None)

# Now you can use that object everywhere
#artist = network.get_artist("System of a Down")
#artist.shout("<3")


#track = network.get_track("Iron Maiden", "The Nomad")
#track.love()
#track.add_tags(("awesome", "favorite"))