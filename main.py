import datetime

# --- Student Information ---
student_name = "Mohan Nagare"
college_name = "Isbm Coe"
roll_no = 03
experiment = "Experiment 2: Cloud & GitHub Integration"

# Get current execution time
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- Terminal Output Design ---
print("=" * 55)
print(" ☁️  GOOGLE CLOUD PLATFORM SECURE EXECUTION ☁️")
print("=" * 55)
print(f"  Student Name : {student_name}")
print(f"  College      : {college_name}")
print(f"  Task         : {experiment}")
print(f"  Timestamp    : {current_time}")
print("-" * 55)
print("  [SYSTEM CHECK]: Code securely pulled from GitHub.")
print("  [STATUS]: Executing flawlessly on Google Cloud Shell.")
print("=" * 55)
