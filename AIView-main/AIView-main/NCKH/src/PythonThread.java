import java.io.*;

public class PythonThread implements Runnable{
    @Override
    public void run() {
    	System.out.println(System.getProperty("user.dir"));
    	
        String pythonScriptPath = System.getProperty("user.dir")+"\\AIView-main\\NCKH\\src\\CodePython\\test.py"; // thay doi file
        String py= "C:\\Users\\Administrator\\eclipse-workspace\\AIView-main\\AIView-main\\NCKH\\src\\CodePython\\hi.py";
        System.out.println(pythonScriptPath);
        try {
            //processBuilder cai tien hon process
            ProcessBuilder pb = new ProcessBuilder("C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", py);
            Process process = pb.start();

            InputStream inputStream = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

            String line;
            while ((line = reader.readLine()) != null) { //Kiem tra python chay den dau
                System.out.println(line);
            }

        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }
}

