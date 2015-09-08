class clarification {
	public static void main(String args[])
		throws java.io.IOException {
			
			char ch, ignore, answer = 'K';

			do {
				System.out.println("I'm thinking of a letter between A and Z.");
				System.out.print("Can you guess it?: ");

				ch = (char) System.in.read();

				do {
					ignore = (char) System.in.read();
				} while (ignore != '\n');

				if (ch == answer) System.out.println("Right");
				else {
					System.out.print("...Sorry, you're ");
					if (ch < answer) System.out.println("You're too low!");
					else System.out.println("You're too high!");
					System.out.println("Try again!");
				}
			} while (ch != answer);
		}
}
