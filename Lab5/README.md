# File Backup Scheduler

## Overview

This Python script provides a simple file backup solution by scheduling periodic backups using the `schedule` library. 
Users can specify the source and destination folders for backup, and the script will automatically perform the backup at the scheduled time.

## Features

- **Backup Functionality:** Copies the contents of the source folder to the destination folder.
- **Scheduling:** Utilizes the `schedule` library to schedule daily backups at a specified time.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/Adv-Python-Lab.git
   cd Adv-Python-Lab
   cd Lab%
   ```

2. **Configure Source and Destination Folders:**
 - Open the file_backup.py script.
 - Replace "add your desired path" with the actual paths of your source and destination folders.

3. **Run the Program:**
   ```bash
   python file_backup.py
   ```
4. **Scheduled Backup:**
The backup is scheduled to run every day at 10:07 PM. Adjust the scheduled time in the script if needed.

5. **Stop the Scheduler:**
Press Ctrl+C to stop the backup scheduler.
## Notes
 - Ensure Python 3.x is installed on your system.
 - Adjust the source and destination folder paths according to your requirements.
 - The schedule library allows for flexible scheduling options. Customize the script to suit your backup frequency and timing preferences.

Feel free to explore and modify the script based on your backup needs.
