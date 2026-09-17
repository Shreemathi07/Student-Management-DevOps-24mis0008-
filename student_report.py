import os
import sys

def process_academic_records():
    # Concrete datasets wrapped cleanly in tuples to run flawlessly
    student_records = [
        {"id": "STU001", "name": "Alice Johnson", "marks": (85, 90, 78, 92, 88)},
        {"id": "STU002", "name": "Bob Smith", "marks": (70, 65, 80, 72, 75)},
        {"id": "STU003", "name": "Charlie Brown", "marks": (45, 50, 48, 55, 42)},
        {"id": "STU004", "name": "Diana Prince", "marks": (95, 98, 92, 96, 94)},
        {"id": "STU005", "name": "Evan Wright", "marks": (60, 58, 62, 65, 59)}
    ]
    
    total_students = len(student_records)
    passed_students = 0
    failed_students = 0
    class_total_score = 0
    total_courses = 5
    
    report_content = []
    report_content.append("=" * 60)
    report_content.append("    STUDENT MANAGEMENT & ACADEMIC PERFORMANCE SYSTEM REPORT")
    report_content.append("=" * 60 + "\n")
    report_content.append(f"Total Registered Students Evaluated: {total_students}")
    report_content.append("-" * 60)
    
    for student in student_records:
        avg_score = sum(student["marks"]) / total_courses
        class_total_score += avg_score
        
        if avg_score >= 90: grade = 'A'
        elif avg_score >= 80: grade = 'B'
        elif avg_score >= 70: grade = 'C'
        elif avg_score >= 50: grade = 'D'
        else: grade = 'F'
        
        status = "PASSED"
        if avg_score < 50:
            status = "FAILED"
            failed_students += 1
        else:
            passed_students += 1
            
        report_content.append(
            f"ID: {student['id']} | Name: {student['name']:<15} | Avg: {avg_score:>6.2f}% | Grade: {grade} | Status: {status}"
        )
        
    class_average = class_total_score / total_students
    pass_rate = (passed_students / total_students) * 100
    
    report_content.append("-" * 60)
    report_content.append("                     SUMMARY STATISTICS")
    report_content.append("-" * 60)
    report_content.append(f"Overall Class Performance Average : {class_average:.2f}%")
    report_content.append(f"Total Academic Passes             : {passed_students}")
    report_content.append(f"Total Academic Failures           : {failed_students}")
    report_content.append(f"System Final Pass Rate            : {pass_rate:.2f}%")
    report_content.append("=" * 60)
    
    output_filename = "academic_summary.txt"
    try:
        with open(output_filename, "w") as report_file:
            report_file.write("\n".join(report_content))
        print(f"[SUCCESS] Academic report successfully written to {output_filename}")
    except IOError as e:
        print(f"[ERROR] Failed to write report file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    process_academic_records()
