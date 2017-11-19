#!/bin/bash
# Assumeing your rocketchat dontainer folder is /var/docker-data/chat
DATE=`date +%Y-%m-%d`
BACKUP_PATH=$1
echo "Backing up RocketChat docker folder..."
echo "tar -czphf $BACKUP_PATH/rocketchat-$DATE.tar.gz /var/docker-data/chat"
tar -czphf $BACKUP_PATH/rocketchat-$DATE.tar.gz /var/docker-data/chat