//Main class that houses the main method, entry point to the program
public class EMS {
    //main method is static so we are not dependent on an object of EMS. its just the entry point
    //Know protected vs public vs private
    public static void main(String [] args) {
        System.out.println("Hello World")
    } 
}


class Employee { // int float double string char
	private int id;
	private String name;
	private double salary; 
	private Department dept; //custom class 
}

class Department {
	private int id;
	private String deptName;
}