public class Truck extends Vehicle{
    public Truck(String r) {
        super(r);
    }
    public Truck(String r, String m, String o) {
        super(r,m,o);
    }
    @Override
    public void checkPollutionStatus() {
        if(compare(25,0.8,1000))
            setPollutionStatus("PASS");
        else 
            setPollutionStatus("FAIL");
    }
}