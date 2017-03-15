
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.GroupLayout;
import javax.swing.LayoutStyle;

public class TTT extends JFrame {
	TTTMain main = new TTTMain();

	public TTT() {
		initComponents();
	}

	public void button1ActionPerformed(ActionEvent e) {
		if (button1.getText().equals("")) {
			if (main.playerTurn == true) {
				button1.setText("X");
				main.b1="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button1.setText("O");
				main.b1="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button2ActionPerformed(ActionEvent e) {
		if (button2.getText().equals("")) {
			if (main.playerTurn == true) {
				button2.setText("X");
				main.b2="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button2.setText("O");
				main.checkforwin();
				main.b2="O";
				main.playerTurn = true;
			}
		}
	}

	public void button3ActionPerformed(ActionEvent e) {
		if (button3.getText().equals("")) {
			if (main.playerTurn == true) {
				button3.setText("X");
				main.b3="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button3.setText("O");
				main.b3="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button4ActionPerformed(ActionEvent e) {
		if (button4.getText().equals("")) {
			if (main.playerTurn == true) {
				button4.setText("X");
				main.b4="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button4.setText("O");
				main.b4="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button5ActionPerformed(ActionEvent e) {
		if (button5.getText().equals("")) {
			if (main.playerTurn == true) {
				button5.setText("X");
				main.b5="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button5.setText("O");
				main.b5="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button6ActionPerformed(ActionEvent e) {
		if (button6.getText().equals("")) {
			if (main.playerTurn == true) {
				button6.setText("X");
				main.b6="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button6.setText("O");
				main.b6="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button7ActionPerformed(ActionEvent e) {
		if (button7.getText().equals("")) {
			if (main.playerTurn == true) {
				button7.setText("X");
				main.b7="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button7.setText("O");
				main.b7="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button8ActionPerformed(ActionEvent e) {
		if (button8.getText().equals("")) {
			if (main.playerTurn == true) {
				button8.setText("X");
				main.b8="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button8.setText("O");
				main.b8="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void button9ActionPerformed(ActionEvent e) {
		if (button9.getText().equals("")) {
			if (main.playerTurn == true) {
				button9.setText("X");
				main.b9="X";
				main.checkforwin();
				main.playerTurn = false;
			} else {
				button9.setText("O");
				main.b9="O";
				main.checkforwin();
				main.playerTurn = true;
			}
		}
	}

	public void initComponents() {
		button1 = new JButton();
		button2 = new JButton();
		button3 = new JButton();
		button4 = new JButton();
		button5 = new JButton();
		button6 = new JButton();
		button7 = new JButton();
		button8 = new JButton();
		button9 = new JButton();

		// ======== this ========
		setTitle("Tic Tac Toe");
		Container contentPane = getContentPane();

		// ---- button1 ----
		button1.setText("");
		button1.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button1ActionPerformed(e);
			}
		});

		// ---- button2 ----
		button2.setText("");
		button2.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button2ActionPerformed(e);
			}
		});

		// ---- button3 ----
		button3.setText("");
		button3.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button3ActionPerformed(e);
			}
		});

		// ---- button4 ----
		button4.setText("");
		button4.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button4ActionPerformed(e);
			}
		});

		// ---- button5 ----
		button5.setText("");
		button5.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button5ActionPerformed(e);
			}
		});

		// ---- button6 ----
		button6.setText("");
		button6.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button6ActionPerformed(e);
			}
		});

		// ---- button7 ----
		button7.setText("");
		button7.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button7ActionPerformed(e);
			}
		});

		// ---- button8 ----
		button8.setText("");
		button8.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button8ActionPerformed(e);
			}
		});

		// ---- button9 ----
		button9.setText("");
		button9.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				button9ActionPerformed(e);
			}
		});

		GroupLayout contentPaneLayout = new GroupLayout(contentPane);
		contentPane.setLayout(contentPaneLayout);
		contentPaneLayout
				.setHorizontalGroup(contentPaneLayout
						.createParallelGroup()
						.addGroup(
								contentPaneLayout
										.createSequentialGroup()
										.addContainerGap()
										.addGroup(
												contentPaneLayout
														.createParallelGroup()
														.addGroup(
																contentPaneLayout
																		.createSequentialGroup()
																		.addComponent(
																				button1,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button2,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button3,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE))
														.addGroup(
																contentPaneLayout
																		.createSequentialGroup()
																		.addComponent(
																				button4,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button5,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button6,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE))
														.addGroup(
																contentPaneLayout
																		.createSequentialGroup()
																		.addComponent(
																				button7,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button8,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)
																		.addPreferredGap(
																				LayoutStyle.ComponentPlacement.RELATED)
																		.addComponent(
																				button9,
																				GroupLayout.PREFERRED_SIZE,
																				55,
																				GroupLayout.PREFERRED_SIZE)))
										.addContainerGap(11, Short.MAX_VALUE)));
		contentPaneLayout
		.setVerticalGroup(contentPaneLayout
				.createParallelGroup()
				.addGroup(
						contentPaneLayout
								.createSequentialGroup()
								.addContainerGap()
								.addGroup(
										contentPaneLayout
												.createParallelGroup(
														GroupLayout.Alignment.BASELINE)
												.addComponent(
														button1,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button2,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button3,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE))
								.addPreferredGap(
										LayoutStyle.ComponentPlacement.RELATED)
								.addGroup(
										contentPaneLayout
												.createParallelGroup(
														GroupLayout.Alignment.BASELINE)
												.addComponent(
														button4,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button5,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button6,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE))
								.addPreferredGap(
										LayoutStyle.ComponentPlacement.RELATED)
								.addGroup(
										contentPaneLayout
												.createParallelGroup(
														GroupLayout.Alignment.BASELINE)
												.addComponent(
														button7,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button8,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE)
												.addComponent(
														button9,
														GroupLayout.PREFERRED_SIZE,
														55,
														GroupLayout.PREFERRED_SIZE))
								.addContainerGap(15, Short.MAX_VALUE)));
		pack();
		setLocationRelativeTo(getOwner());
	}

	public JButton button1;
	public JButton button2;
	public JButton button3;
	public JButton button4;
	public JButton button5;
	public JButton button6;
	public JButton button7;
	public JButton button8;
	public JButton button9;
}