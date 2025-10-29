public class EncapsulationDemo {
    public static void main(String[] args) {
        Student s = new Student();
        s.setName("Alice");
        s.setAge(25);
        System.out.println(s.getName() + " is " + s.getAge() + " years old.");
        // System.out.println(s.name); if uncomment will break
    }
}


