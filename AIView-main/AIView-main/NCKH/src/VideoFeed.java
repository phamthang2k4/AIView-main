//import com.github.sarxos.webcam.Webcam;
//
//import javax.swing.*;
//import java.awt.*;
//
//public class VideoFeed  extends  Thread{
//    private Webcam webcam;
//    private JLabel imageHolder;
//    public VideoFeed(Webcam webcam, JLabel imageHolder){
//        this.webcam= webcam;
//        this.imageHolder= imageHolder;
//    }
//    public void run(){
//        while (true){
//            Image image = webcam.getImage();
//            System.out.println("FPS: "+ webcam.getFPS());
//            imageHolder.setIcon(new ImageIcon(image));
//            try {
//                Thread.sleep(80);
//            } catch (InterruptedException e) {
//                throw new RuntimeException(e);
//            }
//        }
//    }
//}
