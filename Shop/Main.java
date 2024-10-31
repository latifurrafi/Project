public class Main {
    public static void main(String[] args) {
        Agora agora = new Agora("agora@example.com", "123 Main St");
        Book book = new Book(29.99, 123456789);

        System.out.println("Shop Name: " + agora.getName());
        System.out.println("Shop Email: " + agora.getEmail());
        System.out.println("Shop Location: " + agora.getLocation());
        System.out.println("Book Price: $" + book.getUnitPrice());
        System.out.println("Book ISBN: " + book.getIsbnNumber());
    }
}

