import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.GridLayout;
import java.awt.FlowLayout;
import java.awt.BorderLayout;
import java.awt.event.*;
import java.io.File;
import java.util.Scanner;

public class GUI extends JFrame {
    private static File file = null;

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
                } catch (Exception e1) {
                    JOptionPane.showMessageDialog(null, "Error in opening file", "error", JOptionPane.ERROR_MESSAGE);
                    return;
                }
                try {
                    Tmodel.setRowCount(0);
                while (sc.hasNextLine()) {
                    String s = sc.nextLine();
                    int lastIndex = s.lastIndexOf("-");
                    // String hash = s.substring(lastIndex + 1).trim();
                    // String actual = s.substring(0, lastIndex).trim();
                    String hash = s.substring(lastIndex + 2);
                    String actual = s.substring(0, lastIndex-1);
                    if (hash.equals(MD5.getHash(actual))) {
                            Tmodel.addRow(new Object[]{actual, "verified"});
                        } else 
                            Tmodel.addRow(new Object[]{actual, "not verified"});   
                  }
                } catch (Exception e) {
                    e.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Error in processing file "+file.getName(), "error", JOptionPane.ERROR_MESSAGE);
                    sc.close();
                    return;
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
}  