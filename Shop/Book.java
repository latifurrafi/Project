public class Book extends Item {
    private int isbnNumber;

    public Book(double unitPrice, int isbnNumber) {
        super(unitPrice);
        this.isbnNumber = isbnNumber;
    }

    public int getIsbnNumber() {
        return isbnNumber;
    }
}
