==========================================================
  D A T A S E T / D A T A B A S E  D E S C R I P T I O N
==========================================================

(template based on https://arxiv.org/abs/1803.09010)


* Name of the dataset/database:

Meta data on (album and single) releases to Spotify
(2015/10/30 - 2018/6/26)

==========================================================
1. MOTIVATION
==========================================================

1.1  For what purpose was the dataset created?
     Was there a specific task in mind? Was there
     a specific gap that needed to be filled?
     Please provide a description.

     Studying (potential changes) in the composition of
     new releases (i.e., music albums, singles) that
     became available on Spotify during the observation period.


1.2  Who created this dataset
     (e.g., which team, research group) and on behalf of
     which entity (e.g., company, institution, organization)?

     Hannes Datta, Tilburg University.
     By means of web scraping http://everynoise.com/sorting_hat_closet/
     on 6 July 2018.

1.3  Who funded the creation of the dataset?
     If there is an associated grant, please provide
     the name of the grantor and the grant name and number.

     Netherlands Organisation for Scientific Research,
     Veni grant by Hannes Datta (NWO 453-09-004).

1.4  Any other comments?

     None.

==========================================================
2. COMPOSITION
==========================================================

2.1  What do the instances that comprise the dataset represent
     (e.g., documents, photos, people, countries)?
     Are there multiple types of instances (e.g., movies,
     users, and ratings; people and interactions between them;
     nodes and edges)?
     Please provide a description.

     Weekly lists with new singles/album releases.

2.2  How many instances are there in total
     (of each type, if appropriate)?

     2,265,666

2.3  Does the dataset contain all possible instances or is it a sample
     (not necessarily random) of instances from a larger set?
     If the dataset is a sample, then what is the larger set?
     Is the sample representative of the larger set
     (e.g., geographic coverage)? If so, please describe how this
     representativeness was validated/verified.
     If it is not representative of the larger set, please describe why not
     (e.g., to cover a more diverse range of instances, because
     instances were withheld or unavailable).

     We believe this list is a complete representation of
     all releases that became available during the
     collection period.

     Everynoise.com is an independent project, bought by 
     Spotify in 2014, to bring insights into "the rankings and genres of
     newly released albums on Spotify" (2020, Daily Dot --> see PDF).
     
     The project "is described by Spotify as an “experimental attempt at an 
     algorithmic organisation of the week’s new releases” (2015, The Guardian
     --> see PDF). The particular section of the website ("sorting hat closet")
     became unavailable towards the end of 2018. The tool relied on the
     Spotify WebAPI to retrieve that data.

2.4  What data does each instance consist of?
     "Raw" data (e.g., unprocessed text or images)
     or features? In either case, please provide a description.

     Date - timestamp (yyyy/mm/dd)
     Artistname - Name of the artist
     Albumname - Name of the album
     Albumid - Spotify Album ID
     Releasetype - Single versus album releases. 
                   The data has four categories, based on whether
     		   the release is (a) a single or an album, and (b)
		   whether the genre of the release is available
		   in the data:
     		   "album": album with genre cluster available
		   "other": album without genre cluster available
		   "album-single": single with genre cluster available
		   "other-single": single without genre cluster available
     Artistrank - Spotify popularity score of artist
                  (probably at time of
                  album release)
     Playcountrank - Number of tracks on the release
     Genre cluster - Genre, as clustered by maintainer of
                     everynoise.com; raw genre names
                     probably come from the web API,
                     but the clustering was done by the
                     website, and not Spotify.


2.5  Is there a label or target associated with each instance?
     If so, please provide a description.

     N/A

2.6  Is any information missing from individual instances?
     If so, please provide a description, explaining why this information is
     missing (e.g., because it was unavailable). This does not include
     intentionally removed information, but might include, e.g., redacted text.

     The genre cluster is not available for all instances.
     Also, artist ranks and playcount ranks are missing
     at times.

2.7  Are relationships between individual instances made
     explicit (e.g., users' movie ratings, social network links)?
     If so, please describe how these relationships are made explicit.

     One can open/retrieve meta data on the albums using the
     Spotify Album ID. One can also directly open the relevant
     albums by pasting

     spotify:album:albumID in the Spotify search bar.

2.8  Are there recommended data splits (e.g., training, development/validation,
     testing)?
     If so, please provide a description of these splits, explaining the
     rationale behind them.

     N/A

2.9  Are there any errors, sources of noise, or redundancies in the dataset?
     If so, please provide a description.

     N/A

2.10 Is the dataset self-contained, or does it link to or otherwise rely on
     external resources (e.g., websites, tweets, other datasets)?
     If it links to or relies on external resources,
     a) are there guarantees that they will exist, and remain constant,
     over time;
     b) are there official archival versions of the complete dataset
     (i.e., including the external resources as they existed at the
     time the dataset was created);
     c) are there any restrictions (e.g., licenses, fees) associated with
     any of the external resources that might apply to a future user?
     Please provide descriptions of all external resources and any restrictions
     associated with them, as well as links or other access points, as
     appropriate.

     The data can be linked to Spotify/Spotify's Web API using
     the Spotify album ID.

2.11 Does the dataset contain data that might be considered confidential
     (e.g., data that is protected by legal privilege or by doctor-patient
     confidentiality, data that includes the content of individuals'
     non-public communications)?
     If so, please provide a description.

     No.

2.12 Does the dataset contain data that, if viewed directly, might be offensive,
     insulting, threatening, or might otherwise cause anxiety?
     If so, please describe why.

     No.

2.13 Does the dataset relate to people?
     If not, you may skip the remaining questions in this section.

     Not strictly; individual music artists can be identified
     by their clear-text names, or through the Spotify
     Album ID identifiers.

2.14 Does the dataset identify any subpopulations (e.g., by age, gender)?
     If so, please describe how these subpopulations are identified and
     provide a description of their respective distributions within the dataset.

     No.

2.15 Is it possible to identify individuals (i.e., one or more natural persons),
     either directly or indirectly (i.e., in combination with other data)
     from the dataset?
     If so, please describe how.

     Yes, music artists that release commercial music to Spotify.

2.16 Does the dataset contain data that might be considered sensitive in
     any way (e.g., data that reveals racial or ethnic origins, sexual
     orientations, religious beliefs, political opinions or union memberships,
     or locations; financial or health data; biometric or genetic data;
     forms of government identification, such as social security numbers;
     criminal history)?
     If so, please provide a description.

     No.

2.17 Any other comments?

     N/A.

==========================================================
3. COLLECTION PROCESS
==========================================================

3.1  How was the data associated with each instance acquired?
     Was the data directly observable (e.g., raw text, movie ratings),
     reported by subjects (e.g., survey responses), or indirectly
     inferred/derived from other data (e.g., part-of-speech tags, model-based
     guesses for age or language)? If data was reported by subjects or indirectly
     inferred/derived from other data, was the data validated/verified?
     If so, please describe how.

     The data was scraped from everynoise.com/sorting_hat_closet
     on 6 July 2018 (within a couple of hours).

     The website itself became unavailable by the end of 2018.

3.2  What mechanisms or procedures were used to collect the data
     (e.g., hardware apparatus or sensor, manual human curation,
     software program, software API)?
     How were these mechanisms or procedures validated?

     Python scripts. The data was inspected upon retrieval
     (e.g., by computing some summary statistics).

3.3  If the dataset is a sample from a larger set, what was the sampling strategy
     (e.g., deterministic, probabilistic with specific sampling probabilities)?

     N/A

3.4  Who was involved in the data collection process (e.g., students,
     crowdworkers, contractors) and how were they compensated (e.g., how
     much were crowdworkers paid)?

     Only the main investigator mentioned above.

3.5  Over what timeframe was the data collected? Does this timeframe
     match the creation timeframe of the data associated with the
     instances (e.g., recent crawl of old news articles)?
     If not, please describe the timeframe in which the data associated with the
     instances was created.

     The data was scraped on the data mentioned above.
     It refers to the time period mentioned above.


3.6  Were any ethical review processes conducted (e.g., by an institutional
     review board)?
     If so, please provide a description of these review processes, including
     the outcomes, as well as a link or other access point to any
     supporting documentation.

     No.

3.7  Does the dataset relate to people?
     If not, you may skip the remainder of the questions in this section.

     Yes. Commercially available music artists, that can
     be identified by their full names.

3.8  Did you collect the data from the individuals in question directly,
     or obtain it via third parties or other sources (e.g., websites)?

     Via everynoise.com.

3.9  Were the individuals in question notified about the data collection?
     If so, please describe(or show with screenshots or other information) how
     notice was provided, and provide a link or other access point to,
     or otherwise reproduce, the exact language of the notification itself.

     No, as these are commercially available music artists.

3.10 Did the individuals in question consent to the collection and use of their
     data?
     If so, please describe (or show with screenshots or other information)
     how consent was requested and provided, and provide a link or other access
     point to, or otherwise reproduce, the exact language to which the
     individuals consented.

     No, as these are commercially available music artists.

3.11 If consent was obtained, were the consenting individuals provided with a
     mechanism to revoke their consent in the future or for certain uses?
     If so, please provide a description, as well as a link or other access
     point to the mechanism (if appropriate).

     N/A

3.12 Has an analysis of the potential impact of the dataset and its use on data
     subjects (e.g., a data protection impact analysis)been conducted?
     If so, please provide a description of this analysis, including the
         outcomes, as well as a link or other access point to any supporting
         documentation.

     N/A

3.13 Any other comments?

     N/A

==========================================================
4. PREPROCESSING/CLEANING/LABELING
==========================================================

4.1  Was any preprocessing/cleaning/labeling of the data done (e.g.,
       discretization or bucketing, tokenization, part-of-speech tagging,
         SIFT feature extraction, removal of instances, processing of
         missing values)? If so, please provide a description. If not, you may skip
         the remainder of the questions in this section.

     The released data was merged from the individual CSV files.
     HTML files with the exact copies of the websites have been archived.
     These raw data files are only available on request.

     The released data set is a combined dataset with all
     CSV files.

     No other preprocessing has been applied.

4.2  Was the "raw" data saved in addition to the
     preprocessed/cleaned/labeled data (e.g., to support unanticipated
     future uses)? If so, please provide a link or other access point to
     the "raw" data.

     Yes, it is also stored in the data's main repository.

4.3  Is the software used to preprocess/clean/label the instances available?
     If so, please provide a link or other access point.

     Python 3.x.

4.4  Any other comments?

     N/A

==========================================================
5. USES
==========================================================

5.1  Has the dataset been used for any tasks already?
     If so, please provide a description.

     Joint research with Nazli Alagoz and George Knox.
     "Platform Incentives and Commercial Music Production".

5.2  Is there a repository that links to any or all papers or systems
     that use the dataset?
     If so, please provide a link or other access point.

     Not at this time.

5.3  What (other) tasks could the dataset be used for?

     N/A

5.4  Is there anything about the composition of the dataset or the way it was
         collected and preprocessed/cleaned/labeled that might impact future uses?
         For example, is there anything that a future user might need to know to
         avoid uses that could result in unfair treatment of individuals or groups
         (e.g., stereotyping, quality of service issues) or other undesirable harms
         (e.g., financial harms, legal risks) If so, please provide a description.
         Is there anything a future user could do to mitigate these undesirable
         harms?

     N/A

5.5  Are there tasks for which the dataset should not be used?
     If so, please provide a description.

     N/A

5.6  Any other comments?

     N/A

==========================================================
6. DISTRIBUTION
==========================================================

6.1  Will the dataset be distributed to third parties outside of the entity
     (e.g., company, institution, organization) on behalf of which the
     dataset was created?
     If so, please provide a description.

     Yes, publicly.

6.2  How will the dataset will be distributed(e.g.,tarball on website, API,
     GitHub)? Does the dataset have a digital object identifier (DOI)?

     Data via:
     Datta, Hannes, 2020, "Meta data on (album and single) releases to Spotify", https://doi.org/10.34894/DX857S, DataverseNL.

     Repository with code:
     https://github.com/hannesdatta/data-spotify-releases

6.3  When will the dataset be distributed?

     After finalization of working paper.

6.4  Will the dataset be distributed under a copyright or other intellectual
     property(IP) license, and/or under applicable terms of use (ToU)?
     If so, please describe this license and/or ToU, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms or
     ToU (Terms of Use), as well as any fees associated with these restrictions.

     CC0 - "Public Domain Dedication".

6.5  Have any third parties imposed IP-based or other restrictions on the
     data associated with the instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms,
     as well as any fees associated with these restrictions.

     No.

6.6  Do any export controls or other regulatory restrictions apply to the
     dataset or to individual instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any supporting documentation.

     No.

6.7  Any other comments?

     N/A

==========================================================
7. MAINTENANCE
==========================================================

7.1  Who is supporting/hosting/maintaining the dataset?

     Hannes Datta
     https://hannesdatta.com

7.2  How can the owner/curator/manager of the dataset be contacted
     (e.g., email address)?

     h.datta@tilburguniversity.edu

7.3  Is there an erratum?
     If so, please provide a link or other access point.

     N/A

7.4  Will the dataset be updated (e.g., to correct labeling errors, add
     new instances, delete instances)?
     If so, please describe how often, by whom, and how updates will
     be communicated to users (e.g., mailing list, GitHub)?

     Maintenance on documentation of the data will be done.
     The raw data as such is final.

7.5  If the dataset relates to people, are there applicable limits on the
     retention of the data associated with the instances
     (e.g., were individuals in question told that their data would be retained
     for a fixed period of time and then deleted)?
     If so, please describe these limits and explain how they will be enforced.

     N/A

7.6  Will older versions of the dataset continue to be
     supported/hosted/maintained?
     If so, please describe how. If not, please describe how its obsolescence
     will be communicated to users.

     The raw data will stay available online.
     Derivates (such as the one published here) may be updated.


7.7  If others want to extend/augment/build on/contribute to the dataset,
     is there a mechanism for them to do so?
     If so, please provide a description. Will these contributions be
     validated/verified?
     If so, please describe how. If not, why not? Is there a process for
     communicating/distributing these contributions to other users?
     If so, please provide a description.

     Contact the maintainer of the dataset, please.

7.8  Any other comments?

     None.
