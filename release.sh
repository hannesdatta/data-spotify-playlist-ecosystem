. credentials.txt
while true; do
    read -p "You are about to update the public/derived version of your data. Do you want to continue? Type yes or no." yn
    case $yn in
        [Yy]* ) java -jar DVUploader.jar -server=https://dataverse.nl -ex=.DS_Store -key=$dataverse_key -verify -did=doi:$doi release/spotify_releases.csv; java -jar DVUploader.jar -server=https://dataverse.nl -ex=.DS_Store -verify -key=$dataverse_key -did=doi:$doi doc/*; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
