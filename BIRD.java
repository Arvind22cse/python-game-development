import java.swing.*;
public class App{
	public static void main(string[] args)throws Exception{
	int bw=360;
	int bh=640;
	JFrame frame=new JFrame("Flappy bird");
	frame.setVisible(true);
	frame.setSize(bw,bh);
	frame.setLocationRelaiveTo(null);
	frame.setResizable(false);
	frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}