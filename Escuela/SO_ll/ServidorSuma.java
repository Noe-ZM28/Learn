import java.net.*;
import java.io.*;
public class ServidorSuma{

public static void main(String []xf){
int x,y,sum;
String a,b;
ServerSocket ss=null;
try{
ss=new ServerSocket(5051);
}
catch(IOException e){}
try{
    Socket s1=ss.accept();
    InputStream is=s1.getInputStream();
    DataInputStream dis=new DataInputStream(is);
    a=dis.readUTF();
    System.out.println("el numero recibido es:"+a);

    Socket s2=ss.accept();
    InputStream is2=s2.getInputStream();
    DataInputStream dis2=new DataInputStream(is2);
    b=dis2.readUTF();
    System.out.println("el numero recibido es:"+b);
   
    x=Integer.parseInt(a);
    y=Integer.parseInt(b);
   
    sum=x+y;

    Socket sc=new Socket("localhost",5052);
    OutputStream os=sc.getOutputStream();
    DataOutputStream dos=new DataOutputStream(os);
    dos.writeUTF("la suma total es:" + sum);

dos.close();
s1.close();
s2.close();
       
}
catch(IOException e){}

}
}