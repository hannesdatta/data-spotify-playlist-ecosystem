# Documentation of "The playlist ecosystem at Spotify"

This is a repository which hosts the source code to prepare the public version of the data set:

Datta, Hannes, 2020, "The playlist ecosystem at Spotify", https://doi.org/10.34894/4UBBAW, DataverseNL.

If you are...
- a (potential) user of the data, you can [download the data](https://doi.org/10.34894/4UBBAW), or view its detailed [documentation here](doc/). 
- part of the maintenance team, you can use this repository to update the dataset or its documentation.
- interested in creating your own reproducible workflows for anonymizing and sharing data with the public, you can use this repository as a template.

<!-- remove if necessary-->
__Note:__ The data set is not released to the public yet (expected mid of 2021). For questions, get in touch via email, please.
<!-- -->

## Overview about the data

This repository consists of two main data collections, administered via the Chartmetric API:

**(1) Database 1, retrieved in 2019-11**

1.1 List of 1.1m playlists on Spotify (+ associated metadata)

1.2 Playlist placements (current and past tracks on a playlist) for the Top 50k playlists in terms of followers

1.3 Time-series data on a playlist's followers for the Top 10k playlists in the data.


**(2) Database 2, retrieved between 2020-04 and 2020-08**

2.1 List of 1.2m playlists on Spotify (+ associated metadata)

2.2 Playlist placements (current and past tracks on a playlist)

Collected for (a) the Top 150k playlists in terms of followers, (b) a random selection of the remaining ("below top 150k") playlists, and (c) playlists identified to serve personalized and semi-personalized recommendations.

2.3 Playlist followers

The database also holds time-series data for a playlist's followers for the Top 150k playlists in the data, see 2.2 (a), and for the playlists identified to serve personalized and semi-personalized recommendations, see 2.2 (c).

2.4 Playlists' and artists' listeners

Information on a playlists' number of monthly listeners (vs. followers), and artists' monthly listeners for artists that appeared on any of the Top 150k playlists in the data, see 2.2 (a).

2.5 Artist fan metrics

Information on the number of followers on Instagram and Deezer for artists that appeared on any of the Top 150k playlists in the data, see 2.2 (a).


The data is stored in new-line separated JSON files, whereby each line holds a self-contains JSON object. Files are split into chunks of ~8GB if the total file sizes exceeds 8 GB.


## Workflow for maintaining the data and its documentation

### Setup

- Obtain a valid API key from Dataverse ("API Token" in the main menu), paste the key in `credentials.txt`.
- Install Java
- Download the most recent version of the [Dataverse uploading tool](https://github.com/GlobalDataverseCommunityConsortium/dataverse-uploader/) (run `bash init.sh` on Mac, or paste the link contained in the file in your browser on Windows)


### File and directory structure

```
├── credentials.txt         <- stores API credentials
├── doc                     <- put any documentation here
│   └── readme-template.txt (start from this template)
├── rawdata-confidential    <- folder with confidential data
├── release                 <- folder with public releases
└── src                     <- source code to transform confidential
                               data for public release
```

### Workflow

* __Archive confidential raw data on Dataverse__: `push_raw.sh` pushes the raw data to Dataverse (done once, `bash push_raw.sh`; or paste code into your command prompt on Windows). Remember to __restrict access to the folder__, by editing the file/directory permissions directly on Dataverse.

* __Add/change data preparation code__ (e.g., to anonymize data) in `src\`; run this code yourself to produce derivate datasets for the (to-be-made public) `release\` folder.

* __Release public versions__ of the data to Dataverse: `release.sh` pushes (updates) to the documentation in `doc\`, or the prepared data set in `release\`.

* Done? Publish your data set on Dataverse (via the web interface).

Note: API keys used in the `.sh` scripts is deprecated.
