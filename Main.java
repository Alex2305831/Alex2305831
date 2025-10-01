import java.util.Scanner;
public class Main{
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            String txt="Right now im practising in Java and i really like it";
            String txt2="Right now im practising in Python and i really like it";
            byte[] result=txt.getBytes();
            System.out.println(result[0]);
            char result2=txt.charAt(27);
            System.out.println(result2);
            do { 
                System.out.println(txt.replaceAll("Java", "Python"));
                break;
            } while (txt.length()<60);
            System.out.println(txt.compareTo(txt2));
            System.out.println("Enter your information below");
            System.out.print("Name:");
            String name=scan.nextLine();
            System.out.print("City:");
            String city=scan.nextLine();
            System.out.print("Age:");
            int age=scan.nextInt();
            System.out.println("Your name is "+name+" you are "+age+" years old and you live in "+city);
        }
    }
}