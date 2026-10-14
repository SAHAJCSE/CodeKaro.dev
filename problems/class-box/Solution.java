import java.util.Scanner;

class Box{
    private int length, breadth, height;

    Box() {
       this.length=0;
this.breadth=0;
this.height=0;
    }

    Box(int length, int breadth, int height) {
this.length=length;
this.breadth=breadth;
this.height=height;
    }

    Box(Box b1) {
this.length=b1.length;
this.breadth=b1.breadth;
this.height=b1.height;
    }

    int getLength() {
 return length; 
}
    int getBreadth() {
 return breadth;
 }
    int getHeight() {
 return height; 
}
    long CalculateVolume() {
 return (long) length*breadth*height; 
}
}
