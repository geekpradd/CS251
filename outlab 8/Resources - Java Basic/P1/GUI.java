import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class GUI extends JFrame {
    private static File file = new File("");

    public GUI() {
        setLayout(new FlowLayout());
        //create table with data
        DefaultTableModel Tmodel = new DefaultTableModel(0,0);
        Tmodel.addColumn("Plain Text");
        // Tmodel.addColumn("Name");
        // Tmodel.addColumn("Hourly Rate");
        Tmodel.addColumn("Verified?");
        JTable table = new JTable(Tmodel);
        JPanel tablepanel = new JPanel(new GridLayout(1,1));
        tablepanel.add(new JScrollPane(table));
        JButton process = new JButton("process");
        JButton select = new JButton("Select File");
        JFileChooser chooser = new JFileChooser();
        tablepanel.setVisible(false);
        select.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent arg0) {
                int returnval = chooser.showOpenDialog(null);
                if (returnval == JFileChooser.APPROVE_OPTION) {
                    file = chooser.getSelectedFile();
                }
            }
        });
        process.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				Scanner sc;
                try {
                    sc = new Scanner(file);
                } catch (FileNotFoundException e1) {
                    JOptionPane.showMessageDialog(null, "Error in opening file", "error", JOptionPane.ERROR_MESSAGE);
                    return;
                }
                while (sc.hasNextLine()) {
                    String s = sc.nextLine();
                    int lastIndex = s.lastIndexOf("-");
                    String hash = s.substring(lastIndex + 1).trim();
                    String actual = s.substring(0, lastIndex).trim();
                    try {
                        if (hash.equals(MD5.getHash(actual))) {
                            Tmodel.addRow(new Object[]{actual, "verified"});
                        } else 
                            Tmodel.addRow(new Object[]{actual, "not verified"});
                    } catch (NoSuchAlgorithmException e) {
                        e.printStackTrace();
                        return;
                    }
                  }
                sc.close();
            tablepanel.setVisible(true);
            pack();    
        }
        });
        //  Tmodel.addRow(new Object[]{"asad", "John"});

        JPanel panel = new JPanel(new GridLayout(2,1));
        panel.add(process);
        panel.add(select);
         this.add(tablepanel, BorderLayout.CENTER);
        this.add(panel,BorderLayout.SOUTH);
        process.setBounds(150, 150, 100, 30);
        
        // table.setBounds(16, 203, 362, 16);
        // table.setShowHorizontalLines(true);
        // table.setShowVerticalLines(true);
        this.setTitle("MD 5 Checker");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);       
        this.pack();
        this.setLocationRelativeTo(null);
        this.setVisible(true);
    }

         
    public static void main(String[] args)
    {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new GUI();
            }
        });
    }    
//     public static void main(String[] args) {
//         JFrame f = new JFrame("MD5 checker"); f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//         JButton select = new JButton("Select File");
//         JButton process = new JButton("Process");
//         JFileChooser chooser = new JFileChooser();
//         DefaultTableModel model = new DefaultTableModel(0,0);
//         // model.addColumn("Plain Text");
//         // model.addColumn("Verified?");
//         model.setColumnIdentifiers(new String[]{"Plain Text", "Verified"});
//         JTable table = new JTable();
//         table.setModel(model);

//         select.addActionListener(new ActionListener() {
//             @Override
//             public void actionPerformed(ActionEvent arg0) {
//                 int returnval = chooser.showOpenDialog(null);
//                 if (returnval == JFileChooser.APPROVE_OPTION) {
//                     file = chooser.getSelectedFile();
//                 }
//             }
//         });

//         process.addActionListener(new ActionListener() {
//             @Override
//             public void actionPerformed(ActionEvent arg0) {
//                 Scanner sc;
//                 try {
//                     sc = new Scanner(file);
//                 } catch (FileNotFoundException e1) {
//                     e1.printStackTrace();
//                        System.out.println(file.getName());
//                     return;
//                 }
//                 System.out.println(file.getName());

//                 while (sc.hasNextLine()) {
//                     String s = sc.nextLine();
//                     int lastIndex = s.lastIndexOf("-");
//                     String hash = s.substring(lastIndex + 1).trim();
//                     String actual = s.substring(0, lastIndex).trim();
//                     try {
//                         if (hash.equals(MD5.getHash(actual))) {
//                             model.addRow(new Object[]{actual, "verified"});
//                             System.out.println(actual+" verified");                
//                         } else 
//                             model.addRow(new Object[]{actual, "not verified"});
//                     } catch (NoSuchAlgorithmException e) {
//                         e.printStackTrace();
//                         return;
//                     }
//                   }
//                 sc.close();
//            }        
//         });
        
//     select.setBounds(150, 100, 100, 30);
//     process.setBounds(150, 150, 100, 30);
//     table.setPreferredScrollableViewportSize(new Dimension(500, 70));
//     table.setFillsViewportHeight(true);
//     JScrollPane scrollPane = new JScrollPane(table);
//     JPanel panel = new JPanel(new GridLayout(1,0));
//     panel.add(scrollPane);
//     panel.setOpaque(true);
//     f.add(select);  
//     f.add(process);  
//     // f.setContentPane(panel);;
//     f.setSize(400,400);  
//     f.setLayout(null);  
//     f.setVisible(true);   
// }  
}  