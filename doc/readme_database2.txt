==========================================================
  D A T A S E T / D A T A B A S E  D E S C R I P T I O N
==========================================================

(template based on https://arxiv.org/abs/1803.09010)


* Name of the dataset/database:

The playlist ecosystem at Spotify - DATABASE 2
(collected via Chartmetric in April - September 2020)


==========================================================
1. MOTIVATION
==========================================================

1.1  For what purpose was the dataset created?
     Was there a specific task in mind? Was there
     a specific gap that needed to be filled?
     Please provide a description.

	After the collection of database 1, and
	building a prototype to measure the power of 
	digital platforms over suppliers of digital content,
	it was decided the data needs to be collected
	again, and complemented with additional data sets.
	
	The data was "seeded" with a list of 1.2m playlists
	(as retrieved via Chartmetric) on 20 April 2020.
	Subsequent data collections were running until September 2020,
	but the data provides only a comprehensive view on the 
	playlist ecosystem up to and including 18 April 2020.
	
	
1.2  Who created this dataset
     (e.g., which team, research group) and on behalf of
      which entity (e.g., company, institution, organization)?

	Hannes Datta, Tilburg University
	

1.3  Who funded the creation of the dataset?
     If there is an associated grant, please provide
     the name of the grantor and the grant name and number.

	Netherlands Organisation for Scientific Research,
	Veni grant by Hannes Datta (NWO 453-09-004).
	
	
1.4  Any other comments?

==========================================================
2. COMPOSITION
==========================================================

2.1  What do the instances that comprise the dataset represent
     (e.g., documents, photos, people, countries)?
     Are there multiple types of instances (e.g., movies,
     users, and ratings; people and interactions between them;
     nodes and edges)?
     Please provide a description.

	The data consists of multiple JSON files. Files
	are clearly numbered. Raw files larger than 9GB
	were split into smaller JSON files. File numbering
	is clearly indicated with a _, after which the file
	number is given.
	
	
	- all-playlists is a collection of 1.2m playlists and 
	associated meta data
	
	- all-curators is a list with meta data on the curators of 
	the playlists
	
	- for the top 150,000 playlists (in terms of followers, approx. 99% follower share):
	
	  o playlist-placements records the current and 
	  past playlist placements (tracks listed on a particular
	  playlist), starting around Oct/Nov 2016 (probably the
	  beginning of the tracking period by Chartmetric.com).
	  
	  o playlist-followers records time series for
	  a playlist's number of followers (daily).
	
	- for a random sample of playlists outside of the top 150,000 in terms of followers
	  (i.e., low-popularity playlists)
	  
	  o playlist-placements-below150k 
	  
	  o playlist-followers-below150k
	  
	
	- for a subset of playlists that were identified to serve recommendations
	  (e.g., fully personalized recommendations via "Discover Weekly",
	  semi-personalized recommendations via mass playlists that can serve
	  personalized content, and artist-based recommendations via "This is..."
	  and "... Radio" playlists.
	  
	  o playlist-placements-recommendations
	  
	  o playlist-followers-recommendations
	
	- social media "fan"/"follower" data for all artists listed
	on any of the top 150k playlists (about 1m artists)
	
	  o fans-instagram
	  o fans-deezer and fans-deezer-missings (some data was missing in the first 
	  retrieval, so it was recollected later)
	  

2.2  How many instances are there in total
     (of each type, if appropriate)?
	 
	 - 1.2m playlists for all-playlists
	 - about 150k for playlist-placements (x2 for current and past placements), and playlist-followers
	 - about 5k playlists that serve recommendations
	 - the size of placements/followers below 150k is unknown
	 - fan data for about 1m artists
	 
2.3  Does the dataset contain all possible instances or is it a sample
     (not necessarily random) of instances from a larger set?
     If the dataset is a sample, then what is the larger set?
     Is the sample representative of the larger set
     (e.g., geographic coverage)? If so, please describe how this
     representativeness was validated/verified.
     If it is not representative of the larger set, please describe why not
     (e.g., to cover a more diverse range of instances, because
     instances were withheld or unavailable).

	The Spotify ecosystem features millions of playlists; we only 
	can observe 1.2m via Chartmetric.
	
	The top 150k selection is selected by the number of followers
	(i.e., a selection of the most popular lists). Using the 1.2m
	lists, one can compute the coverage in terms of followers.
	The below-150k selection is a randomly shuffled list of
	playlists below 150k. The data collection was stopped eventually,
	as enough objects had been collected and data collection
	capacity was used for other means. Because playlist IDs were
	shuffled before data retrieval, this selection is still 
	random.
	
2.4  What data does each instance consist of?
     "Raw" data (e.g., unprocessed text or images)
     or features? In either case, please provide a description.
 
	New-line separated JSON files. The structure of each JSON object
	contains detailed logs on the moment of data retrieval,
	and the associated API endpoints.
	Some larger JSON files (>9GB) are split into multiple files, indicated
	by _, and followed by a number.

2.5  Is there a label or target associated with each instance?
     If so, please provide a description.

	Each instance is labeled either with type, e.g., "all-playlists",
	"playlist-placements", or "playlist-followers", etc.
	
	In comparison to database 1, the playlist-followers object originates from
	Chartmetric's publicly available API.
	
2.6  Is any information missing from individual instances?
     If so, please provide a description, explaining why this information is
     missing (e.g., because it was unavailable). This does not include
     intentionally removed information, but might include, e.g., redacted text.

	Some objects may have been downloaded with errors (shows up
	in each object's status_code; 200 if retrieved correctly).
	
	Each API endpoint has been tried for at least 3-5 times.


2.7  Are relationships between individual instances made
     explicit (e.g., users' movie ratings, social network links)?
     If so, please describe how these relationships are made explicit.

	The objects can be linked using internal Chartmetric IDs for
	each playlist. The dataset also allows linkage to Spotify,
	as it records the actual playlist Spotify IDs.

2.8  Are there recommended data splits (e.g., training, development/validation,
     testing)?
     If so, please provide a description of these splits, explaining the
     rationale behind them.

	 No.
	
2.9  Are there any errors, sources of noise, or redundancies in the dataset?
     If so, please provide a description.

	The placement data contains many duplicates, which will have to be 
	identified after parsing the data. Data quality checks for the raw data are
	not included here.

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

	Links to Spotify, using Spotify IDs for e.g., playlists or artists/tracks.
	The objects also contain image links, and it's not guaranteed these
	links will be continue to be online.
	
2.11 Does the dataset contain data that might be considered confidential
     (e.g., data that is protected by legal privilege or by doctor-patient
     confidentiality, data that includes the content of individuals'
     non-public communications)?
     If so, please provide a description.

	None.
	
2.12 Does the dataset contain data that, if viewed directly, might be offensive,
     insulting, threatening, or might otherwise cause anxiety?
     If so, please describe why.

	None.
	
2.13 Does the dataset relate to people?
     If not, you may skip the remaining questions in this section.

	Music artists and playlist curators. Some of the playlist curators are individual users of Spotify.
	
2.14 Does the dataset identify any subpopulations (e.g., by age, gender)?
     If so, please describe how these subpopulations are identified and
     provide a description of their respective distributions within the dataset.

	No.
	
2.15 Is it possible to identify individuals (i.e., one or more natural persons),
     either directly or indirectly (i.e., in combination with other data)
     from the dataset?
     If so, please describe how.

	Some curators of playlists may be identifiable based on their usernames.


2.16 Does the dataset contain data that might be considered sensitive in
     any way (e.g., data that reveals racial or ethnic origins, sexual
     orientations, religious beliefs, political opinions or union memberships,
     or locations; financial or health data; biometric or genetic data;
     forms of government identification, such as social security numbers;
     criminal history)?
     If so, please provide a description.

	The data reveals the names of playlists created by playlist curators
	on the platform. To the degree that users disclose their ethnic origin,
	sexual orientation, religious beliefs or political opinions, this
	may be reflected in the data. The data set has not been collected
	for this process, and it has not been attempted to identify such dimensions
	from the data.
	
2.17 Any other comments?

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


	Collection via a paid subscription to the Chartmetric API in 2020 (April - September).
	
	Development of a collection crawler ("API Manager"), and concurrent
	storage on MongoDB.
	
	Each JSON object, hence, not only shows the result of the API call,
	but in addition produces a detailed log of the retrieval process.
	
	
3.2  What mechanisms or procedures were used to collect the data
     (e.g., hardware apparatus or sensor, manual human curation,
     software program, software API)?
     How were these mechanisms or procedures validated?

	Data collected on Datta's office computer at Tilburg University.
	Storage was on MongoDB (Atlas), EU-based instance.


3.3  If the dataset is a sample from a larger set, what was the sampling strategy
     (e.g., deterministic, probabilistic with specific sampling probabilities)?

List of "job ids" and associated description of the job (and time of execution).

5e8ea481f23009aa0deed61d get-curators platformpower-recollection-april2020 2020-04-09 04:28 0
5e8f06f3f23009aa0deee120 get-all-playlists platformpower-recollection-april2020 2020-04-09 11:28 0
5e8f0d3cf23009aa0def109e get-fans-instagram student - roy scriptie 2020-04-09 11:55 0 *not included here*
5e901d8134fea5e44fe4fbd7 get-instagram-audience-stats student - roy scriptie 2020-04-10 07:17 0 *not included here*
5e918eadd7d8d6f5c89178ed get-playlist-placements platformpower-recollection-april2020 2020-04-11 09:32 0
5e96fc79d7d8d6f5c8960cce get-playlist-followers platformpower-recollection-april2020 2020-04-15 12:22 0
5ec9749bf66ac93c77ad4af8 get-fans-instagram platformpower-recollection-may2020 2020-05-23 19:08 0
5ee8a858898879247697295d get-fans-deezer platformpower-recollection-may2020 2020-06-16 11:09 0
5f0d7ac466e900572f1272ed get-artist-metadata naz-phd 2020-07-14 09:28 0 *not included here*
5f0d82cd66e900572f13432d get-playlist-placements platformpower-recollection-april2020-bottomk-random 2020-07-14 10:02 0
5f23c576b5f1f17ddbab4b38 get-playlist-placements platformpower-recollection-april2020-reclists-only(july) 2020-07-31 07:17 0
5f441e09a13ca58ff4bac6f7 get-playlist-followers platformpower-recollection-april2020-reclists-only(august) 2020-08-24 20:07 0
5f707f9ea13ca58ff4bb10ab get-fans-deezer platformpower-recollection-september2020-getmissings 2020-09-27 12:03 0


3.4  Who was involved in the data collection process (e.g., students,
     crowdworkers, contractors) and how were they compensated (e.g., how
     much were crowdworkers paid)?

	Hannes Datta.
	
	Students were not actively involved in the collection process. However, they were
	involved when I drafted the data collection strategy (e.g., thinking about 
	which variables to parse).
	
	
3.5  Over what timeframe was the data collected? Does this timeframe
     match the creation timeframe of the data associated with the
     instances (e.g., recent crawl of old news articles)?
     If not, please describe the timeframe in which the data associated with the
     instances was created.

	See time stamps in the log above.
	
3.6  Were any ethical review processes conducted (e.g., by an institutional
     review board)?
     If so, please provide a description of these review processes, including
     the outcomes, as well as a link or other access point to any
     supporting documentation.

	No.


3.7  Does the dataset relate to people?
     If not, you may skip the remainder of the questions in this section.

	Music artists, and curators of playlists.
	
3.8  Did you collect the data from the individuals in question directly,
     or obtain it via third parties or other sources (e.g., websites)?

	Via Chartmetric.com.
	
3.9  Were the individuals in question notified about the data collection?
     If so, please describe(or show with screenshots or other information) how
     notice was provided, and provide a link or other access point to,
     or otherwise reproduce, the exact language of the notification itself.

	Many of the curators in the data are entities in the music industry
	(e.g., music labels, artists, radio stations, etc.). 
	The data also contains the curation decisions of individual users,
	who have agreed to the Spotify Terms of Use that their publicly listed
	playlist data is retrievable via the Spotify Web API, which in turn was
	used by our data provider to disclose the data to us.
	
3.10 Did the individuals in question consent to the collection and use of their
     data?
     If so, please describe (or show with screenshots or other information)
     how consent was requested and provided, and provide a link or other access
     point to, or otherwise reproduce, the exact language to which the
     individuals consented.

	Implicitly, by making their data available to Spotify and their partners.
	
3.11 If consent was obtained, were the consenting individuals provided with a
     mechanism to revoke their consent in the future or for certain uses?
     If so, please provide a description, as well as a link or other access
     point to the mechanism (if appropriate).

	No.
	
3.12 Has an analysis of the potential impact of the dataset and its use on data
     subjects (e.g., a data protection impact analysis) been conducted?
     If so, please provide a description of this analysis, including the
         outcomes, as well as a link or other access point to any supporting
         documentation.

	This data does not, to the best of my knowledge, infringe any
	personal rights of curators or music artists.
	
	As for curators, the data set lists their usernames, and description.
	As for music artists, the data set lists their track releases and 
	associated release dates & acoustic attributes.
	
3.13 Any other comments?

	We include a PDF of the API documentation (as extracted on 21 October 2020).
	The data collection used version 1.2 of the API.
	
==========================================================
4. PREPROCESSING/CLEANING/LABELING
==========================================================

4.1  Was any preprocessing/cleaning/labeling of the data done (e.g.,
     discretization or bucketing, tokenization, part-of-speech tagging,
     SIFT feature extraction, removal of instances, processing of
     missing values)? If so, please provide a description. If not, you may skip
     the remainder of the questions in this section.

	The raw data was retrieved via the Chartmetric API, and is included as is.
	There are three parsing scripts available for each of the main data sets - 
	these select a few key attributes for parsing.
	
4.2  Was the "raw" data saved in addition to the
     preprocessed/cleaned/labeled data (e.g., to support unanticipated
     future uses)? If so, please provide a link or other access point to
     the "raw" data.
	 
	 The raw data is available in JSON files included in this archive.

4.3  Is the software used to preprocess/clean/label the instances available?
     If so, please provide a link or other access point.

	Python 3.7.
	
4.4  Any other comments?


==========================================================
5. USES
==========================================================

5.1  Has the dataset been used for any tasks already?
     If so, please provide a description.

	- Master thesis projects at Tilburg University.
	- Prototype of "platform power" project by Hannes Datta and
	Max J. Pachali.

5.2  Is there a repository that links to any or all papers or systems
     that use the dataset?
     If so, please provide a link or other access point.

	No.
	
5.3  What (other) tasks could the dataset be used for?

	- Investigation of drivers of playlist followers
	- Classification of playlists into types (e.g., mood versus genre)
	- Classification of music labels into types (e.g., major versus indie)
	- Study of how tracks transition from playlists to other playlists

5.4  Is there anything about the composition of the dataset or the way it was
         collected and preprocessed/cleaned/labeled that might impact future uses?
         For example, is there anything that a future user might need to know to
         avoid uses that could result in unfair treatment of individuals or groups
         (e.g., stereotyping, quality of service issues) or other undesirable harms
         (e.g., financial harms, legal risks) If so, please provide a description.
         Is there anything a future user could do to mitigate these undesirable
         harms?
	
	No.
	
5.5  Are there tasks for which the dataset should not be used?
     If so, please provide a description.

	No.
	
5.6  Any other comments?

==========================================================
6. DISTRIBUTION
==========================================================

6.1  Will the dataset be distributed to third parties outside of the entity
     (e.g., company, institution, organization) on behalf of which the
     dataset was created?
     If so, please provide a description.

	 The raw data set will not be distributed to third parties
	 outside of Tilburg University.
	 
	 Derived versions that are GDPR compliant (e.g., 
	 with anonymized user names) can be distributed later on.
	
	
6.2  How will the dataset will be distributed (e.g.,tarball on website, API,
       GitHub)? Does the dataset have a digital object identifier (DOI)?

	Stored for interal use at dataverse (private).
	
	Derived (parsed, and GDPR-compliant versions) will be made public.

6.3  When will the dataset be distributed?

	For now, embargo period of 2 years.
	
6.4  Will the dataset be distributed under a copyright or other intellectual
     property(IP) license, and/or under applicable terms of use (ToU)?
     If so, please describe this license and/or ToU, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms or
         ToU (Terms of Use), as well as any fees associated with these restrictions.

	tba

6.5  Have any third parties imposed IP-based or other restrictions on the
     data associated with the instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms,
     as well as any fees associated with these restrictions.

	Chartmetric.com does not have Terms of Use for data downloaded via their
	API.

6.6  Do any export controls or other regulatory restrictions apply to the
     dataset or to individual instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any supporting documentation.

	No.
	
6.7  Any other comments?

==========================================================
7. MAINTENANCE
==========================================================

7.1  Who is supporting/hosting/maintaining the dataset?

	The data is not being maintained (i.e., not potentially corrected).
	However, future releases of similar data are planned.
	
7.2  How can the owner/curator/manager of the dataset be contacted
     (e.g., email address)?

	h.datta@tilburguniversity.edu.

7.3  Is there an erratum?
     If so, please provide a link or other access point.

7.4  Will the dataset be updated (e.g., to correct labeling errors, add
     new instances, delete instances)?
     If so, please describe how often, by whom, and how updates will
     be communicated to users (e.g., mailing list, GitHub)?

	No.
	
7.5  If the dataset relates to people, are there applicable limits on the
     retention of the data associated with the instances
     (e.g., were individuals in question told that their data would be retained
       for a fixed period of time and then deleted)?
     If so, please describe these limits and explain how they will be enforced.

	Businesses, which - sometimes - overlap with "individuals"  (e.g., music artists,
	curators).
	
7.6  Will older versions of the dataset continue to be
     supported/hosted/maintained?
     If so, please describe how. If not, please describe how its obsolescence
     will be communicated to users.

	No.
	
7.7  If others want to extend/augment/build on/contribute to the dataset,
     is there a mechanism for them to do so?
     If so, please provide a description. Will these contributions be
     validated/verified?
     If so, please describe how. If not, why not? Is there a process for
     communicating/distributing these contributions to other users?
     If so, please provide a description.

	Please provide any code to the community via GitHub (e.g.,
	classification of labels, playlist types).
	
	Please provide any additional data via Dataverse,
	or contact us to provide such data to the community (h.datta@tilburguniversity.edu).
	
7.8  Any other comments?


