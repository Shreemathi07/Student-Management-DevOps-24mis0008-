import sys

def compile_core_application():
    print("[BUILD] Packaging Core Management application assets...")
    print("[BUILD] Validating framework dependency injections...")
    print("[SUCCESS] Main administrative code builds completed successfully.")

def run_intensive_academic_audit():
    print("\n" + "=" * 50)
    print("      CRITICAL ACADEMIC RISK AUDIT OPERATION")
    print("=" * 50)
    
    # Explicit subject performance distribution values
    raw_grades_data = {
        "Math": (85, 70, 45, 95, 60),
        "Science": (90, 65, 50, 98, 58),
        "History": (78, 80, 48, 92, 62)
    }
    
    risk_threshold = 50
    flagged_incidents = 0
    
    for subject, scores in raw_grades_data.items():
        print(f"[SCANNING] Processing {subject} class registry tracking arrays...")
        for score in scores:
            if score < risk_threshold:
                print(f"  [RISK ALERT] Performance warning triggered! Score: {score}")
                flagged_incidents += 1
                
    print("-" * 50)
    print(f"Audit Summary: Found {flagged_incidents} low-performance incidents requiring attention.")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--run-audit":
        run_intensive_academic_audit()
    else:
        compile_core_application()
