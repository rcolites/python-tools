import os

class Logger:
    def log(self, level, context, message): 
        print(f"[{level}] {context}: {message}") 


# Suspicious extensions to look for
SUSPICIOUS_EXTENSIONS = [".exe", ".bat", ".vbs", ".ps1", ".cmd"]


def scan_folder(path, logger): 
    if not os.path.exists(path): 
        logger.log("ERROR", "Scan", f"Path does not exist: {path}") 
        return 

    logger.log("INFO", "Scan", f"Scanning folder: {path}")

    found = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in SUSPICIOUS_EXTENSIONS:
                full_path = os.path.join(root, file)
                logger.log("WARNING", "SuspiciousFile", f"Found: {full_path}")
                found += 1

    if found == 0:
        logger.log("INFO", "Scan", "No suspicious files found.")
    else:
        logger.log("NOTICE", "Scan", f"Total suspicious files: {found}")


# Main logic
if __name__ == "__main__":
    logger = Logger()
    folder_to_scan = ""  # you can change this
    scan_folder(folder_to_scan, logger)
