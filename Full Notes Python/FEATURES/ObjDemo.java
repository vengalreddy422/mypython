class Student
{
	int sno;
	String name;
	float marks;
	String city;
}//Student--Class Name
class ObjDemo 
{
	public static void main(String[] args) 
	{
		Student s=new Student() ; // Object  Creation 
		s.sno=10;
		s.name="JG";
		s.marks=34.56f;
		System.out.println(s.sno+" "+s.name+" "+s.marks);
		s.city="HYD";
		System.out.println(s.sno+" "+s.name+" "+s.marks+" "+s.city);
		s.colname="JNTU";
	}
}
