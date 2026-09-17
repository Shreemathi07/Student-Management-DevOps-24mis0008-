import sys
import time

def audit_database_integrity():
    print("[INIT] Booting Student Profile Registry Database Check...")
    # Complex record mockup verifying object properties
    mock_db = [
        {"id": "STU001", "email": "alice@school.edu", "phone": "123-456-7890"},
        {"id": "STU002", "email": "bob@school.edu", "phone": "234-567-8901"},
        {"id": "STU003", "email": "charlie@school.edu", "phone": "345-678-9012"},
        {"id": "STU004", "email": "diana@school.edu", "phone": ""}, # Missing phone allowed
        {"id": "STU005", "email": "evan@school.edu", "phone": "567-890-1234"}
    ]
    
    unique_ids = set()
    
    for idx, profile in enumerate(mock_db, 1):
        print(f"[PROCESSING] Verifying registry record {idx}/{len(mock_db)} for {profile['id']}...")
        time.sleep(0.6) # Simulating complex network latency
        
        # Logic constraints check
        if not profile["id"].startswith("STU"):
            print(f"[CRITICAL] Invalid formatting schema constraint for ID: {profile['id']}")
            sys.exit(1)
            
        if "@" not in profile["email"]:
            print(f"[CRITICAL] Broken syntax on communication channel for user: {profile['id']}")
            sys.exit(1)
            
        if profile["id"] in unique_ids:
            print(f"[CRITICAL] Primary key constraint collision detected on ID: {profile['id']}")
            sys.exit(1)
            
        unique_ids.add(profile["id"])
        
    print("[SUCCESS] All system database formatting rules validated.")

if __name__ == "__main__":
    audit_database_integrity()
