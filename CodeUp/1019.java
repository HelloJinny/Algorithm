import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        		String str = sc.next();
        
        		String[] arr = str.split("\\.");
        
        		int year = Integer.valueOf(arr[0]);
       		int month = Integer.valueOf(arr[1]);
        		int day = Integer.valueOf(arr[2]);
        
        		System.out.printf("%04d.%02d.%02d", year, month, day);

	}

}