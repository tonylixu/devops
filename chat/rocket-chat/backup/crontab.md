```bash
# Rocketchat backup
# First day of each month, 3AM
0 3 1 * * /bin/bash /var/scripts/rocketchat/rocketchat-full-backup.sh /var/docker-data/backups/rocketchat/full-backups

# Every Sunday, 4AM
0 4 * * Sun /bin/bash /var/scripts/rocketchat/rocketchat-weekly-level-0-backup.sh /var/docker-data/backups/rocketchat/incremental-backups

# Every Monday-Satruday, 4AM
0 4 * * 1-6 /bin/bash /var/scripts/rocketchat/rocketchat-daily-level-1-backup.sh /var/docker-data/backups/rocketchat/incremental-backups
```