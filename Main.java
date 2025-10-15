import java.util.Scanner;
public class Main{
    static void myMethod(String txt){
        System.out.println(txt.replaceAll("my","your"));
    }
    public static void main(String[] args) {
        myMethod("This is my text");
        Scanner scan=new Scanner(System.in);
        System.out.print("Please type your text again to solve something:");
        String txt=scan.nextLine();
        System.out.println(txt);
        System.out.print("Type a random number to see his multiplication operation until 10:");
        int x=scan.nextInt();
        for (int i=1;i<=10;i++){
            System.out.println(x+" * "+i+" = "+x*i);
        }
        int y=(int)(Math.random()*11);
        System.out.println(y);
        switch (y){
            case 0:
               System.out.print("You lost you succeded 0");
               break;
            case 1:
                System.out.print("You win you succeded 1");
                break;
            case 3:
                System.out.print("You have 3 attempts because you succeded 3");
                break;
            case 5:
                System.out.print("You succeded 5 so the program is success");
                break;
            case 7:
                System.out.print("You are lucky because you succeded 7");
                break;
            case 10:
                System.out.print("You succeded 10 so you are smart you are 10/10");
                break;
            default:
                System.out.print("Number with no meaning");
        }
    }
}