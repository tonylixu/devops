#!/bin/bash
# Assumeing your rocketchat dontainer folder is /var/docker-data/chat
DATE=`date +%Y-%m-%d`
BACKUP_PATH=$1

# Create level-1 backups
echo "Creating rocketchat-level-0-backup.snar from rocketchat-level-0-backup.snar.bak"
echo "cp $BACKUP_PATH/rocketchat-level-0-backup.snar.bak $BACKUP_PATH/rocketchat-level-1-backup-$DATE.snar"
cp $BACKUP_PATH/rocketchat-level-0-backup.snar.bak $BACKUP_PATH/rocketchat-level-1-backup-$DATE.snar
echo "Making level-1 backups..."
echo "tar --listed-incremental $BACKUP_PATH/rocketchat-level-1-backup.snar -czphf $BACKUP_PATH/rocketchat-level-1-$DATE.tar.gz /var/docker-data/chat"
tar --listed-incremental $BACKUP_PATH/rocketchat-level-1-backup-$DATE.snar -czphf $BACKUP_PATH/rocketchat-level-1-$DATE.tar.gz /var/docker-data/chat
