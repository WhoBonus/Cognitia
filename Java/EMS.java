//Main class that houses the main method, entry point to the program
import java.util.*;

public class EMS {
    //main method is static so we are not dependent on an object of EMS. its just the entry point
    //Know protected vs public vs private
    public static void main(String [] args) {
        System.out.println("Employee Management System");
        Employee[] empArr = new Employee[10];
        //linked list is better for this application. Arrays are fixed in size. Use list
        //list is an interface. What is an interface?
        //Employee new Employee();
        //new means new object of what ttype
        //variables on the stack, object on the heap
        //gentrix is type safety, you could add a student to this list. Angle bracket
        ArrayList<Employee> empList = new ArrayList(); //object type on the right hand side of = is the same type as the referency type. Non polymorphic
        //this is polymorhpic bc the object type is the child type
        //When to use linkedlist vs Arraylist vs Array?
        List<Employee> empListt = new ArrayList<>(); //polymorphism
        List<Employee> empListtt = new LinkedList<>(); //polymorhiphs
        
        
        
        populate(empListtt);
        
        displayAllEmployees(empListtt);
        
        //remove employee THEN print
        modifyEmployee(empListtt, 102, 95000);
        displayAllEmployees(empListtt);
        
        //modify employee THEN print
        deleteEmployee(empListtt, 101);
        displayAllEmployees(empListtt);
        
        //try deleting nonexistent
        deleteEmployee(empListtt, 999);
    } 
    
    //what is a constructor? 
    private static void populate(List<Employee> empListtt) {
    	Department d1 = new Department (1, "HR");
    	Department d2 = new Department (1, "IT");
    	Employee e1 = new Employee (101, "Anthony", 90000, d1);
    	Employee e2 = new Employee (102, "Bob", 80000, d2);
    	Employee e3 = new Employee (103, "Charlie", 60000, d3);
    	empListtt.add(e1);
    	empListtt.add(e2);
    	empListtt.add(e3);
    	
    	
    	
    	
    	
    }
    
    
    
    //static can only be called in a static context
    private static void displayAllEmployees (List<Employee> empListtt) {
    	//for (int i = 0; i<empListtt.size(); i++) {
    	//	
    	//}
    	
    	//more efficient method
    	for (Employee emp:empListtt) {
    		System.out.println(emp);
    	}
    }
    
 
    
    //Modify elements. Find specific ID but customize salary
    private static void modifyEmployee (List<Employee> empListtt, int id, int newSalary) {
    	for (Employee emp : empListtt) {
    		if (emp.getId() == id) {
    			emp.setSalary(newSalary);
    			System.out.println("SALARY UPDATED");
    			return;
    		}
    		
    	}
    	System.out.println("Emp not found");
    }
    
    private static void deleteEmployee (List<Employee> empListtt, int id) {
    	Iterator<Employee> iterator = empListtt.iterator();
        
    	//iterate thru employees
        while (iterator.hasNext()) {
            Employee emp = iterator.next(); 
            
            if (emp.getId() == id) {
                iterator.remove();
                System.out.println("Employee " + id + " deleted.");
                return;
            }
        }
    	System.out.println("Employee not found");
    }
    
    // == this compares references not string values
    //I can also do ignore case
    private static boolean compDept(Employee emp1, Employee emp2) {
 
        return emp1.getDept().getDeptName().equals(emp2.getDept().getDeptName());
    }
}


//every class extend the object class IMPLICILTLY
class Employee extends Object { // prims: int float double string char
	private int id;
	private String name;
	private double salary; 
	private Department dept; //custom class 
	
	
	
	public Employee(int id, String name, double salary, Department dept) {
		super();
		this.id = id;
		this.name = name;
		this.salary = salary;
		this.dept = dept;
	}

	//setters and getters
	//no amibiguity so this isnt needed
	public int getId() {
		return id;
		//or return this.id
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	public Department getDept() {
		return dept;
	}

	public void setDept(Department dept) {
		this.dept = dept;
	}

	//override the inherited tostring method
	@Override
	public String toString() {
		return "Employee [id=" + id + ", name=" + name + ", salary=" + salary + ", dept=" + dept + "]";
	}
	
	
}

class Department {
	private int id;
	private String deptName;
	
	//constructor used to initialize the object. Constructor parametes can be anything, but you can use "this" if its same
	public Department (int id, String deptName) { //these are local variables which live in the stack
		//this references the object reference held in heap
		this.id = id;
		this.deptName = deptName;
	}
	
	/* public Department (int idd, String deptNamee) {
		
		//id references the private vars above
		//this.id = id;
		
		//altern
		id = idd;
		deptName = deptNamee;
	} */
	
	
	@Override
	public String toString() {
		return "Department [id=" + id + ", deptName=" + deptName + "]";
	}

	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getDeptName() {
		return deptName;
	}
	public void setDeptName(String deptName) {
		this.deptName = deptName;
	}	
}

//Overloading vs Overwriting: Overloading is the modify method with same name in same class. OVerwriting deals with an inherited method

