import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import java.util.Comparator;
public class PollutionCheck{
    static private ArrayList<Vehicle> vehicle;
    public static void main(String args[]){
        File veh = new File(args[0]);
        File pol = new File(args[1]);
        File que = new File(args[2]);
        try {
            readVehicles(veh);
            readPollution(pol);
            // for(Vehicle x: vehicle) System.out.println(x);
            Scanner sc = new Scanner(que);
            while(sc.hasNextLine()) {
                handle_query(sc.nextLine().trim());
            }
        }
        catch(Exception e) {}
        
    }   

    public static void readVehicles(File file) throws Exception {
        vehicle = new ArrayList<>();
        Scanner sc = new Scanner(file);
        while(sc.hasNextLine()) {
            String[] entry = sc.nextLine().split(",");
            if(entry[entry.length-1].trim().equals("Car")) {
                // MHA569, Hyundai, Chen Wang, Car
                vehicle.add(new Car(entry[0].trim(),entry[1].trim(),entry[2].trim()));
            }
            else vehicle.add(new Truck(entry[0].trim(),entry[1].trim(),entry[2].trim()));
        }
        Collections.sort(vehicle, new Comparator<Vehicle>() {
            @Override
            public int compare(Vehicle o1, Vehicle o2) {
                return o1.getRegNo().compareTo(o2.getRegNo());
            }
        });
    }

    public static void readPollution(File file) throws Exception{
        Scanner sc = new Scanner(file);
        while(sc.hasNextLine()) {
            // HRY712, 26, 0.5, 278
            String[] entry = sc.nextLine().split(",");
            int index = Collections.binarySearch(vehicle, new Vehicle(entry[0].trim()), new Comparator<Vehicle>() {
                @Override
                public int compare(Vehicle o1, Vehicle o2) {
                    return o1.getRegNo().compareTo(o2.getRegNo());
                }
            });
            if(index>=0)
                vehicle.get(index).setPollutionLevel(Double.parseDouble(entry[1].trim()),Double.parseDouble(entry[2].trim()),Double.parseDouble(entry[3].trim()));
        }
    }

    public static void handle_query(String q) {
        int index = Collections.binarySearch(vehicle, new Vehicle(q), new Comparator<Vehicle>() {
            @Override
            public int compare(Vehicle o1, Vehicle o2) {
                return o1.getRegNo().compareTo(o2.getRegNo());
            }
        });
        if(index>=0)
            System.out.println(vehicle.get(index).getPollutionStatus());
        else
        System.out.println("NOT REGISTERED");
    }
}