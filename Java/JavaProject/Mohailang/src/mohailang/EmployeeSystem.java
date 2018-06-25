package mohailang;

import java.io.Serializable;

public class EmployeeSystem implements Serializable {

    public int id;
    public String name;
    public String address;
    public double salary;

    public EmployeeSystem(int id,String name,String address,double salary){
        this.id = id;
        this.name = name;
        this.address = address;
        this.salary = salary;
    }
}

