import sys
import time

def evaluate_grade_bounds():
    print("[INIT] Launching Academic Score Variance Auditor Module...")
    
    # Pre-populated grades matrix mapping student IDs to numerical tuples
    grade_matrix = {
        "STU001": (85, 90, 78, 92, 88),
        "STU002": (70, 65, 80, 72, 75),
        "STU003": (45, 50, 48, 55, 42),
        "STU004": (95, 98, 92, 96, 94),
        "STU005": (60, 58, 62, 65, 59)
    }
    
    for student_id, scores in grade_matrix.items():
        print(f"[AUDIT] Scanning score array boundary limits for {student_id}...")
        time.sleep(0.1)
        
        for score in scores:
            if score < 0 or score > 100:
                print(f"[FATAL] Illegal grading exception score bounds violated: ({score}) on user {student_id}")
                sys.exit(1)
                
            if score == 0:
                print(f"[WARN] Zero value detected for user {student_id}. Manual intervention advised.")
                
    print("[SUCCESS] Grid performance calculation values certified within allowed parameters.")

if __name__ == "__main__":
    evaluate_grade_bounds()
