#!/bin/bash
# Assumeing your rocketchat dontainer folder is /var/docker-data/chat
DATE=`date +%Y-%m-%d`
BACKUP_PATH=$1

# Create level-0 backups
echo "Backing up files..."
echo "tar --listed-incremental $BACKUP_PATH/rocketchat-level-0-backup.snar -czphf $BACKUP_PATH/rocketchat-level-0-$DATE.tar.gz  /var/docker-data/chat"
tar --listed-incremental $BACKUP_PATH/rocketchat-level-0-backup.snar -czphf $BACKUP_PATH/rocketchat-level-0-$DATE.tar.gz  /var/docker-data/chat
echo "Making copy of rocketchat-level-0-backup.snar..."
echo "cp $BACKUP_PATH/rocketchat-level-0-backup.snar $BACKUP_PATH/rocketchat-level-0-backup.snar.bak"
cp $BACKUP_PATH/rocketchat-level-0-backup.snar $BACKUP_PATH/rocketchat-level-0-backup.snar.bak
