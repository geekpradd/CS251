public class Car extends Vehicle{
    public Car(String r) {
        super(r);
    }
    public Car(String r, String m, String o) {
        super(r,m,o);
    }

    @Override
    public void checkPollutionStatus() {
        if(compare(15,0.5,750))
            setPollutionStatus("PASS");
        else 
            setPollutionStatus("FAIL");
    }
}