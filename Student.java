public class Student {

    // Private attributes
    private String name;
    private String studentId;
    private double grade;

    // Constructor
    public Student(String name, String studentId, double grade) {
        this.name = name;
        this.studentId = studentId;
        this.grade = grade;
    }

    // Getter for name
    public String getName() {
        return name;
    }

    // Getter for studentId
    public String getStudentId() {
        return studentId;
    }

    // Getter for grade
    public double getGrade() {
        return grade;
    }

    // Setter for grade
    public void setGrade(double grade) {
        this.grade = grade;
    }

    // Display student information
    public void displayInfo() {
        System.out.println("Name: " + name +
            " | ID: " + studentId +
            " | Grade: " + grade);
    }

    // Main method
    public static void main(String[] args) {

        // Create two Student objects
        Student student1 = new Student(
            "Juan Dela Cruz", "2026-001", 90.0
        );

        Student student2 = new Student(
            "Maria Santos", "2026-002", 88.5
        );

        // Change the first student's grade
        student1.setGrade(92.0);

        // Display information
        student1.displayInfo();
        student2.displayInfo();
    }
}
