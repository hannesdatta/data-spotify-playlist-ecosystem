# Makefile for \raw-parse of the platform power project
# by Hannes Datta
# requires GNU Make

TEMP_DIR = ../temp
OUTPUT_DIR = ../release/2020_11_23
EXT_DIR = ../rawdata-confidential

all: parse

parse: $(OUTPUT_DIR)/all-playlists.csv $(OUTPUT_DIR)/playlist-followers.csv $(OUTPUT_DIR)/playlist-followers-recommendations.csv $(OUTPUT_DIR)/playlist-placements.csv $(OUTPUT_DIR)/playlist-placements-below150k.csv $(OUTPUT_DIR)/playlist-placements-recommendations.csv $(OUTPUT_DIR)/fans-instagram.csv $(OUTPUT_DIR)/fans-deezer.csv $(OUTPUT_DIR)/fans-deezer-missings.csv

###### BUILD COMMANDS ######

# parse raw playlist data
$(OUTPUT_DIR)/all-playlists.csv: parse_allplaylists.py
	python.exe parse_allplaylists.py $(EXT_DIR)/database2_2020_04/all-playlists.json $(OUTPUT_DIR)/all-playlists.csv

# parse followers
$(OUTPUT_DIR)/playlist-followers.csv: parse_followers.py 
	python.exe parse_followers.py "$(EXT_DIR)/database2_2020_04/playlist-followers_*" $(OUTPUT_DIR)/playlist-followers.csv

# parse followers of rec' playlists
$(OUTPUT_DIR)/playlist-followers-recommendations.csv: parse_followers.py $(EXT_DIR)/database2_2020_04/playlist-followers-recommendations.json
	python.exe parse_followers.py $(EXT_DIR)/database2_2020_04/playlist-followers-recommendations.json $(OUTPUT_DIR)/playlist-followers-recommendations.csv

# parse track placements on playlists (top 150k)
$(OUTPUT_DIR)/playlist-placements.csv: parse_placements.py
	python.exe parse_placements.py "$(EXT_DIR)/database2_2020_04/playlist-placements_*" $(OUTPUT_DIR)/playlist-placements.csv

# parse track placements on playlists (bottom, NOT top 150k)
$(OUTPUT_DIR)/playlist-placements-below150k.csv: parse_placements.py
	python.exe parse_placements.py "$(EXT_DIR)/database2_2020_04/playlist-placements-below150k_*" $(OUTPUT_DIR)/playlist-placements-below150k.csv

# parse track placements on bottom (rec' playlists) playlists
$(OUTPUT_DIR)/playlist-placements-recommendations.csv: parse_placements.py
	python.exe parse_placements.py "$(EXT_DIR)/database2_2020_04/playlist-placements-recommendations_*" $(OUTPUT_DIR)/playlist-placements-recommendations.csv

# parse instagram followers
$(OUTPUT_DIR)/fans-instagram.csv: parse_fans.py $(EXT_DIR)/database2_2020_04/fans-instagram.json
	python.exe parse_fans.py $(EXT_DIR)/database2_2020_04/fans-instagram.json $(OUTPUT_DIR)/fans-instagram.csv

# parse deezer followers
$(OUTPUT_DIR)/fans-deezer.csv: parse_fans.py $(EXT_DIR)/database2_2020_04/fans-deezer.json
	python.exe parse_fans.py $(EXT_DIR)/database2_2020_04/fans-deezer.json $(OUTPUT_DIR)/fans-deezer.csv

# parse deezer followers (missings)
$(OUTPUT_DIR)/fans-deezer-missings.csv: parse_fans.py $(EXT_DIR)/database2_2020_04/fans-deezer-missings.json
	python.exe parse_fans.py $(EXT_DIR)/database2_2020_04/fans-deezer-missings.json $(OUTPUT_DIR)/fans-deezer-missings.csv


#$(OUTPUT_DIR)/chartmetric.zip: zip.py parse
#	python zip.py