import os

# 1. The path to your Janitor's diary
log_file = "janitor.log"

def display_report():
    if os.path.exists(log_file):
        print("\n" + "="*40)
        print("📜 OFFICIAL JANITOR AUDIT REPORT")
        print("="*40)
        
        # 2. Open with utf-8 to handle any hidden characters safely
        with open(log_file, "r", encoding="utf-8") as diary:
            lines = diary.readlines()
            
            # 3. Only show the most recent 10 actions to keep it clean
            recent_logs = lines[-10:]
            
            if not recent_logs:
                print("The log file is currently empty.")
            else:
                for line in recent_logs:
                    # Clean up the line for a nice display
                    print(line.strip())
        
        print("="*40 + "\n")
    else:
        print(f"❌ Error: {log_file} not found. Run janitor.py first!")

if __name__ == "__main__":
    display_report()