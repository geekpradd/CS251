import java.lang.Boolean;
public class Vehicle {
    private String regNo;
    private String manufacturer;
    private String owner;
    private double co2;
    private double co;
    private double hc;
    private String pollutionStatus = "PENDING";

    public Vehicle(String r) {
        regNo = r;
    }
    public Vehicle(String r, String m, String o) {
        regNo = r;
        manufacturer = m;
        owner = o;
        co2 = 0;
        co = 0;
        hc  = 0;
        pollutionStatus = "PENDING";
    }

    public boolean compare(double c2, double c,double h){
        return (co2<=c2)&&(co<=c)&&(hc<=h);
    }

    public void setPollutionStatus(String s) {
        pollutionStatus = s;
    }
    public String getPollutionStatus() {
        return pollutionStatus;
    }
    public String getRegNo() {
        return regNo;
    }
    public void setPollutionLevel(double c2, double c, double h) {
        co2 = c2;
        co = c;
        hc = h;
        checkPollutionStatus();
    }

    public void checkPollutionStatus(){
        
    }

    public String toString() {
       return "Reg No: "+regNo + "\nManufacturer: "+manufacturer+"\nOwner: "+owner+"\nPollution Status: "+pollutionStatus; 
    }
}