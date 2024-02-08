# file backup task
import schedule
import time
import shutil

def backup(source_folder, dest_folder):
    try:
        print("Performing backup...")
        shutil.copytree(source_folder,dest_folder)
        print("Backup successful!")
    except Exception as e:
        print(f"Backup failed: {e}")

def main():
    source_folder = "add your desired path"
    dest_folder = "add your desired path"

    # Schedule the backup to run every day at 6:30 PM
    schedule.every().day.at('10:07').do(backup, source_folder, dest_folder)
    print("Backup scheduler started. Press Ctrl+C to exit.")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Backup scheduler stopped.")

if __name__ == "__main__":
    main()
