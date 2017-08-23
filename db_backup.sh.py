#!/bin/sh

########################
#   POSTGRES CONFIGS   #
########################
# PG_USERNAME='db username'
# PG_PASSWORD='db password'
# PG_DBNAME='db name'
PG_HOST='127.0.0.1'
PG_PORT=5432

#########################
#  FILES & ZIPS  #
#########################

ZIP=gzip
FILE="backup_$(date +%Y%m%d_%H%M%S).gz"
DIR='/var/opt/backup/pgsql/'
filename=${DIR}${FILE}

pg_dump postgresql://${PG_USERNAME}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/${PG_DBNAME} | ${ZIP} > "${filename}"
