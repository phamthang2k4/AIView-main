//import com.github.sarxos.webcam.Webcam;
//import com.github.sarxos.webcam.WebcamPanel;
//import java.awt.*;
//public class WebcamGUI{
//    private AppView appView;
//    public WebcamGUI(AppView appView){
//        this.appView= appView;
//        this.init();
//    }
//    private void init(){
//        this.turnCam();
//    }
//    private void turnCam(){
//        final Webcam webcam= Webcam.getDefault();
//        webcam.setViewSize(new Dimension(640,480));
//
//        WebcamPanel panel1= new WebcamPanel(webcam);
//        panel1.setFPSDisplayed(true);
//        panel1.setImageSizeDisplayed(true);
//        panel1.setMirrored(true);
//        appView.remove(appView.getStartButton());
//        webcam.open();
//        appView.add(panel1);
//        appView.revalidate();
//        appView.repaint();
////        VideoFeed video= new VideoFeed(webcam, imageHolder);
////        video.start();
//    }
//}