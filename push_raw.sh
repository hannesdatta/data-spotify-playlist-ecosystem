. credentials.txt
while true; do
    read -p "You are about to store the raw data publicly. Remember to make such data confidential. Do you want to continue? Type yes or no." yn
    case $yn in
        [Yy]* ) java -jar DVUploader.jar -server=https://dataverse.nl -ex=.DS_Store -key=$dataverse_key -did=doi:10.34894/DX857S -recurse rawdata-confidential; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
