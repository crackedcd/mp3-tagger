from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
from mp3_tagger.id3 import ID3FrameStream, ID3FrameV2, VERSION_2, VERSION_BOTH
import sys
import os
import shutil

rootDir = "E:/music/my_car"
newDir = "E:/music/my_car_new"
for lists in os.listdir(rootDir): 
	filename = os.path.join(rootDir, lists) 

	# Create MP3File instance.
	if filename.endswith('.mp3'):
		mp3 = MP3File(filename)

		# Get all tags.
		tags = mp3.get_tags()
		# print("-------------------------------------------")
		# print("{} => {}".format(filename, tags))
		artist = "anonymous"
		song = "unknown"
		if 'ID3TagV2' in tags:
			tagv2 = tags['ID3TagV2']
			if 'artist' in tagv2:
				artist = tagv2['artist'].strip(b'\x00'.decode())
			if 'song' in tagv2:
				song = tagv2['song'].strip(b'\x00'.decode())
		name = "{} - {}".format(artist, song)
		newfilename = os.path.join(newDir, name)
		try:
			shutil.copyfile(filename, newfilename)
			print("DONE MOVE <<{}>> TO <<{}.mp3>>".format(filename, newfilename))
		except Exception as e:
			print("FAIL MOVE <<{}>> TO <<{}.mp3>>".format(filename, newfilename))
			print(e)
