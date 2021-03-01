import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String word = scan.next();

		String[] array_words = new String[word.length()];		
		array_words = word.split("");
		
		for (int i = 0; i < word.length(); i++)
			System.out.printf("'%s'\n",array_words[i]);
		
	}

}
