import datetime

# Replace log file name
startTime = datetime.datetime.now()
try:
    with open("sample_log_anonymized.log", "r", encoding="utf-8") as f:
        for line in f:
            if "ACLLOG-5-ACLLOG_FLOW_INTERVAL" in line:
                print(line)
except FileNotFoundError:
    print("Error: The file 'sample_log_anonymized.log' was not found.")
except IOError as e:
    print(f"Error: An I/O error occurred: {e}")
endTime = datetime.datetime.now()
elapsedTime = endTime - startTime
print("Time Elapsed: " + str(elapsedTime))
