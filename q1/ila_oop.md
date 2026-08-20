# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation

The pillar, encapsulation, can be used in the sari-sari store inventory system by bundling
individual product data, such as stocks and costs, into classes to safeguard critical business
information. This object-oriented approach protects properties like item_name and stock_count
by making them private and inaccessible to outside tampering. Instead, the data is modified
securely through methods like sell_item() and restock_item(), which automatically prevent
negative numbers or invalid entries. By applying these rules, the sari-sari store inventory
system can keep financial records financial records accurate and free from accidental
calculation errors. Lastly, the use of this pillar creates a clean, organized program
structure that is easy to maintain and expand as the store grows.

PSEUDOCODE:

class Product:

    def __init__(self, name, price, stock):
        self.__name = name         # Private property
        self.__price = price       # Private property
        self.__stock = stock       # Private property
    
    def sell(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        return False

    def get_stock(self):
        return self.__stock

### 2. Abstraction
To manage store operations cleanly, abstraction, one of the 4 pillars, hides the internal
complexities of transaction management and stock calculations behind a simple interface like a
sales tracker or inventory manager class. The user or cashier only interacts with high-level
methods like checkout_item(product_id) or generate_daily_report(), completely unaware of the
complex loops and file-saving operations running behind the scenes. This improves design by
reducing cognitive overload for the developer and isolating core business logic from routine
database updates.

SIMPLE DIAGRAM:

          [ Cashier User ]
                 │
                 │  Presses "Checkout" button
                 V
     _________________________
     │  SalesTracker Class   │
     |_______________________|
     │   checkout_item()     │  <- What user sees & uses; high-level methods
     |-----------------------| [ Abstraction Barrier ]
     │   calculate_tax()     │  <- Hidden complexity
     │   save_to_file()      │  <- Hidden complexity
     |_______________________|


### 3. Inheritance

Inheritance can be used in the system to create categories of inventory from a general base
item, minimizing redundant code as the store expands. The implementation of this pillar
involves a parent Product class that contains shared properties, such as product name and
price, which are inherited by child classes; for instance, a SpoilableProduct class can
inherit pricing logic while introducing its own expiration date attribute. Similarly, a
BulkItem class can reuse the same properties but add a whole sale discount rate for items sold
by the case or bundle. This structure ensures that whenever a new category of goods is
introduced, developers only need to program the differences rather than the entire system from
scratch

SIMPLE DIAGRAM:

            ____________________________
            |     Product (Base)       |--> Shares: name, price, get_details()
            ----------------------------
                          ^
               ___________|__________
              |                      |
     _____________________ _____________________
     │ PerishableProduct │ │   BulkPackItem    │ --> Inherits base properties
     --------------------- ---------------------    Adds unique specialized logic
     Adds: expiration       Adds: box_quantity


### 4. Polymorphism
Polymorphism can be used in the sari-sari store system to execute a single action, such as
checking inventory or calculating total costs, differently depending on the type of product
being processed. This mechanism relies on a shared method that is defined in a parent Product
class and overridden by child classes. When the system loops through the entire stock, an
instruction triggers expiration warning and standard listings for canned goods. This improves
program organization because the inventory management interface interacts with all items
uniformly without complex conditional statements to guess each product's subcategory.

PSEUDOCODE:

    // Define distinct object behaviors
    CLASS Product
        METHOD display()
            PRINT "Standard Sari-Sari Item"
        END METHOD
    END CLASS

    CLASS PerishableProduct INHERITS Product
         METHOD display()
             PRINT "Perishable Item: Check expiration date!"
         END METHOD
    END CLASS

    // Polymorphism in action
    START
        DECLARE inventory = [ NEW Product(), NEW PerishableProduct() ]
   
        FOR EACH item IN inventory DO
            CALL item.display() // Automatically runs the correct version
        END FOR
    END

## Reflection

Out of the four pillars of OOP, I believe that encapsulation is the one which will have the
most helpful effect on the enhancement of the sari-sari store inventory management system
because with the help of encapsulation, the sari-sari store inventory management system will
be able to organize the relevant product information in its objects, including the product
name, price, quantity, and expiration date. Also, with the help of this pillar, access to the
data can be controlled by certain methods and rules; for instance, instead of being changed by
any user, the quantity of each product can be modified only by the methods for adding or
removing inventory. It will improve the security of the data, since any mistakes in changing
the information about the quantity of each product can be prevented in this way. Lastly, using
encapsulation, changes to the inventory information can be made within one class only.
