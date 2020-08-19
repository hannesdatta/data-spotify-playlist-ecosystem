require(data.table)

fns<-list.files(path='../rawdata-confidential/', pattern='*.csv', full.names=T)

dts<-lapply(fns, fread, encoding='UTF-8')

dt <- rbindlist(dts)

dt[,albumname:=gsub('\"\"', '', albumname)]
dt[,artistname:=gsub('\"\"', '', artistname)]
dt[, genre:=gsub('[|]$', '', genre)]
dt[, genre:=gsub('[;]$', '', genre)]
dt[, releasetype:=gsub('[-]$', '', releasetype)]
dt[artistrank=='-', artistrank:=NA]

setnames(dt, 'genre', 'genre_cluster')

setcolorder(dt, c('date', 'artistname', 'albumname', 'albumid', 'releasetype', 'artistrank','playcountrank', 'genre_cluster'))
fwrite(dt, '../release/spotify_releases.csv',row.names=F)




