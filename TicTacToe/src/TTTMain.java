import javax.swing.*;
import java.awt.*;

public class TTTMain extends JFrame {
	public static boolean playerTurn = true;
	public static boolean playerWon = false;
	public static boolean computerWon = false;
	public static String b1="", b2="", b3="", b4="", b5="", b6="", b7="", b8="", b9="";
	
	public static TTT board = new TTT();
	
	public static void main(String[] args){
		if(board.isVisible()==false){
			board.setVisible(true);
		}
	}
	public static void checkforwin(){
		if(b7.equals("X")&&b1.equals("X")&&b4.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b2.equals("X")&&b5.equals("X")&&b8.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b3.equals("X")&&b6.equals("X")&&b9.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b1.equals("X")&&b2.equals("X")&&b3.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b4.equals("X")&&b5.equals("X")&&b6.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b7.equals("X")&&b8.equals("X")&&b9.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b7.equals("X")&&b5.equals("X")&&b3.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b5.equals("X")&&b1.equals("X")&&b9.equals("X")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 1 Won!");
			System.exit(0);
		}
		if(b7.equals("O")&&b1.equals("O")&&b4.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b2.equals("O")&&b5.equals("O")&&b8.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b3.equals("O")&&b6.equals("O")&&b9.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b1.equals("O")&&b2.equals("O")&&b3.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b4.equals("O")&&b5.equals("X")&&b6.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b7.equals("O")&&b8.equals("O")&&b9.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b7.equals("O")&&b5.equals("O")&&b3.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		if(b5.equals("O")&&b1.equals("O")&&b9.equals("O")){
			playerWon = true;
			computerWon = false;
			JOptionPane.showInputDialog("Player 2 Won!");
			System.exit(0);
		}
		checktie();
	}
	public static void checktie(){
		if(b1.equals("O")||b1.equals("X")){
			if(b2.equals("O")||b2.equals("X")){
				if(b3.equals("O")||b3.equals("X")){
					if(b4.equals("O")||b4.equals("X")){
						if(b5.equals("O")||b5.equals("X")){
							if(b6.equals("O")||b6.equals("X")){
								if(b7.equals("O")||b7.equals("X")){
									if(b8.equals("O")||b8.equals("X")){
										if(b9.equals("O")||b9.equals("X")){
											playerWon=false;
											computerWon=false;
											JOptionPane.showInputDialog("Its a tie!");
											System.exit(0);
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
