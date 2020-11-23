set /p DOI=<doi.txt
ECHO %DOI%
java -jar DVUploader.jar -server=https://dataverse.nl -ex=.DS_Store -ex=.gitkeep -key=%DATAVERSE_TOKEN% -did=doi:%DOI% -recurse rawdata-confidential