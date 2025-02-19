import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class EOF {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int linenumber = 1;
        
        while(sc.hasNext()){
            String line = sc.nextLine();
            System.out.println(linenumber + " " + line);
            linenumber++;
        }
        
        sc.close(); 
    }
}