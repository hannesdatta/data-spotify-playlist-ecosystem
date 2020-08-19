# Documentation of "(Album and single) releases to Spotify (2015/10/30 - 2018/6/26)"

This is a repository which hosts the source code to prepare the public version of the data set:

Datta, Hannes, 2020, "(Album and single) releases to Spotify", https://doi.org/10.34894/DX857S, DataverseNL.

If you are a (potential) user of the data, please directly access its [documentation here](doc/readme-data.txt). Use this repository to maintain the dataset, or jump-start your own workflow to release data to the public.

Maintainer: h.datta@tilburguniversity.edu

<!-- remove if necessary-->
__Note:__ The data set is not released to the public yet (expected end of 2020). For questions, get in touch via email, please.
<!-- -->

## Setup

* Obtain a valid API key from Dataverse ("API Token" in the main menu), paste the key in `credentials.txt`.
* Install Java
* Download the most recent version of the [Dataverse uploading tool](https://github.com/GlobalDataverseCommunityConsortium/dataverse-uploader/) (run `bash init.sh` on Mac, or paste the link contained in the file in your browser on Windows)


## File and directory structure

```
├── credentials.txt         <- stores API credentials
├── doc                     <- put any documentation here
│   └── readme-template.txt (start from this template)
├── rawdata-confidential    <- folder with confidential data
├── release                 <- folder with public releases
└── src                     <- source code to transform confidential
                               data for public release
```

## Workflow

* __Archive confidential raw data on Dataverse__: `push_raw.sh` pushes the raw data to Dataverse (done once, `bash push_raw.sh`; or paste code into your command prompt on Windows). Remember to __restrict access to the folder__, by editing the file/directory permissions directly on Dataverse.

* __Add/change data preparation code__ (e.g., to anonymize data) in `src\`; run this code yourself to produce derivate datasets for the (to-be-made public) `release\` folder.

* __Release public versions__ of the data to Dataverse: `release.sh` pushes (updates) to the documentation in `doc\`, or the prepared data set in `release\`.

* Done? Publish your data set on Dataverse (via the web interface).

Note: API keys used in the `.sh` scripts is deprecated.
