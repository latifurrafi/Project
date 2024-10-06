// Abstract Class Example
abstract class BankAccount {
    protected double balance;

    // Constructor
    public BankAccount(double balance) {
        this.balance = balance;
    }

    // Abstract method for withdrawal, to be implemented by subclasses
    public abstract void withdraw(double amount);

    // Concrete method for depositing money
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: $" + amount);
    }

    // Method to display balance
    public void displayBalance() {
        System.out.println("Current balance: $" + balance);
    }
}

// Savings Account Class (Inherits from BankAccount)
class SavingsAccount extends BankAccount {
    private double interestRate;

    public SavingsAccount(double balance, double interestRate) {
        super(balance);
        this.interestRate = interestRate;
    }

    @Override
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Insufficient funds");
        }
    }

    public void addInterest() {
        balance += balance * interestRate;
        System.out.println("Interest added");
    }
}

// Interface Example
interface AccountActions {
    void withdraw(double amount);
    void deposit(double amount);
}

// Implementing the Interface in a Class
class CheckingAccount implements AccountActions {
    private double balance;

    public CheckingAccount(double balance) {
        this.balance = balance;
    }

    @Override
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
        } else {
            System.out.println("Insufficient funds");
        }
    }

    @Override
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: $" + amount);
    }

    public void displayBalance() {
        System.out.println("Current balance: $" + balance);
    }
}

// Main Class
public class Main {
    public static void main(String[] args) {
        // Using abstract class
        BankAccount savings = new SavingsAccount(1000, 0.05);
        savings.deposit(500);
        savings.withdraw(200);
        savings.displayBalance();

        // Using interface
        AccountActions checking = new CheckingAccount(1000);
        checking.deposit(500);
        checking.withdraw(300);
        ((CheckingAccount) checking).displayBalance();
    }
}
