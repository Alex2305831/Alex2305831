import java.util.Scanner;
public class Main{
    static void Method(String cars){
        System.out.println("The best cars is "+cars);
    }
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            int pin_code=1234;
            int attempts=2;
            System.out.print("Type your pin code to continue if its wrong type again:");
            int user_type=scan.nextInt();
            while(user_type!=pin_code){
                attempts-=1;
                System.out.print("Type again you have "+attempts+" attempts left:");
                user_type=scan.nextInt();
                if(attempts==0){
                    System.out.print("Too bad you are out of attempts");
                    break;
                }
            }
            if(user_type==pin_code){
                System.out.println("Great this is your pin code lets continue");
                }
        
        String[] names=new String[4];
        names[1]="Nick";
        System.out.print(names[1]+" ");
        System.out.println(names.length);
        Method("Bmw"+", Mercedes "+"and Audi");
        System.out.print("Type a number of rows:");
        int rows=scan.nextInt();
        for(int i=0;i<=rows;i++){
            for(int j=0;j<=i;j++){
                System.out.print("*");
            }
            System.out.print("\n");
        }
            }
    }
}