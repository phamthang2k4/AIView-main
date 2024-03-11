import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class AppView extends JFrame {
    private JPanel mainWindow;
    private JButton startButton;
    
    public JPanel getMainWindow() {
        return mainWindow;
    }
    
    public JButton getStartButton() {
        return startButton;
    }
    
    public AppView() {
        this.setTitle("Test");
        this.setSize(720,540);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLocationRelativeTo(null);
        
        // Tạo JPanel mới để làm contentPane
        mainWindow = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                // Vẽ hình ảnh làm hình nền
                Image image = new ImageIcon(".//imges//background_car.jpg").getImage();
                g.drawImage(image, 0, 0, getWidth(), getHeight(), this);
            }
        };
        
        // Sử dụng GridBagLayout cho mainWindow
        mainWindow.setLayout(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        
        // Khởi tạo nút "Start" và cấu hình vị trí của nút
        startButton = new JButton("Start");
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(50, 0, 0, 0); // Đặt khoảng cách từ trên xuống
        gbc.anchor = GridBagConstraints.CENTER;
        mainWindow.add(startButton, gbc); // Thêm nút "Start" vào mainWindow
        
        // Khởi tạo cửa sổ
        init();
        this.setVisible(true);
    }
    
    private void init() {
        this.setContentPane(mainWindow);
        ActionListener ac = new AppController(this);
        startButton.addActionListener(ac);
    }
}