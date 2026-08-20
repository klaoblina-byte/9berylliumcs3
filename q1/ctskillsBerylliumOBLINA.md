# Computational Thinking Exercise
## [Smart School Canteen Queue]
**Name:** Karmela Liane A. Oblina
**Section:** 9 - Beryllium
**Last Name:** Oblina
**Date:** 18/08/2026

## Step 1: Identify the Big Problem

## Main Problem: 

The PSHS school canteen suffers a big problem from overcrowding, especially during lunch break, and slow service due to indecisive students, inefficient ordering, manual payment processing, and lack of real-time tracking of items.

## Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Delayed Decision-Making at the Counter

2. Slow Manual Computation of Payment During Checkout

3. Lack of Real-Time Tracking of Items

4. Overcrowding and Poor Queue Management

## Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

    | Sub-Problem   |    CT Skill     |      Example Solution

    Delayed         |   Abstraction   |Create a physical or digital
    Decision-Making |The abstraction  |menu near the counter and 
    at the Counter  |skill helps      |along the outer part of where
                     prevent delayed  |the queue will be. The menu
                     decision-making  |should be composed of the 
                     at the counter by|items correctly categorized, 
                     focusing only on |its prices, and visual icons.
                     the most         |Irrelevant details, such as 
                     important        |ingredients, should be 
                     information      |avoided as it would lead to 
                     needed to make a |longer decision-making. 
                     decision. It     |Therefore, students can make 
                     reduces confusion|rapid choices before reaching
                     and mental       |the counter.
                     overload,        |
                     allowing staff to|
                     respond to       |
                     customers quickly|
                     and confidently  |


    Slow Manual    |Algorithm Design  |Build a sequential algorithm
    Computation of | Algorithm Design |for a simple checkout
    Payment During |helps prevent slow|interface for the cashiers.
    Checkout       |manual computation|The algorithm is simply:
                   |of payment during |
                   |checkout by       |1. Choose selected items
                   |providing         |2. Calculate sum of items
                   |a clear, step-by- |3. Input cash received
                   |step process for  |4. Calculate change- Cash-Sum
                   |calculating the   |5. Display output
                   |total, discounts, |6. Print Reciept
                   |and change. This  |
                   |makes computations|
                   |faster and more   |
                   |accurate, reducing|
                   |errors and        |
                  |shortening customer|
                   |waiting time.     |


    Lack of Real-  | Pattern Recognition |Track historical data to
    Time Tracking  |                     |recognize patterns of
    of Items       |Pattern Recognition  |which items sell out the
                   |helps address the    |fastest during the first
                   |lack of real-time    |half hour of the lunch 
                   |movement, such as    |period. Using these 
                   |frequently sold or   |patterns, establish a
                   |low-stock items. This|digital notification to
                   |allows staff to      |alarm staff to restock or
                   |monitor item         |take off a specific item
                   |availability more    |in the menu. Additionally,
                   |efficiently and      |establish an automated
                   |quickly recognize    |digital rule that if the
                   |when stock needs to  |stock level is less than
                   |be updated or        |5 units, send an alert to
                   |replenished          |kitchen staff to prepare 
                   |                     |more.


    Overcrowding   |   Decomposition    |Break the large queues and
    and Poor Queue |Decomposition helps |overcrowding problem by:
    Management     |address overcrowding|
                   |and poor queue      |1. Making sure that there
                   |management by       |are at least three cashiers
                   |breaking the problem|in every counter, ensuring
                   |into smaller parts, |that the queues will be
                   |such as identifying |broken down into shorter
                   |customer flow,      |ones.
                   |waiting areas, and  |
                   |service times. This |2.Another three lanes for
                   |makes it easier to  |picking up the food and
                   |find the cause of   |at least 2 staff are
                   |overcrowding and    |assigned to each lane.
                   |organize the queue  |
                   |more efficiently.   |3. The menus are placed
                   |                    |along the queues so    
                   |                    |students can pick while
                   |                    |they are in line. The same
                   |                    |menus can also be placed in
                   |                    |another corner, big enough
                   |                    |so that overcrowding won't
                   |                    |occur.


## Step 4: Algorithmic Solution

##Selected Sub-Problem: Lack of Real-Time Tracking of Items

##PSEUDOCODE

START

Set total_sum = 0
Set items_list = empty list

LOOP
    Ask user for item_name
    IF item_name is empty THEN
        BREAK LOOP
    ENDIF

    Ask user for item_price
    Add item_price to total_sum
    Add (item_name, item_price) to items_list
ENDLOOP

Display total_sum

LOOP
    Ask user for cash_received
    IF cash_received >= total_sum THEN
        BREAK LOOP
    ELSE
        Display "Insufficient payment error"
    ENDIF
ENDLOOP

Compute change = cash_received - total_sum

Display "Payment Accepted"
Display change

Display receipt header
FOR EACH item IN items_list
    Display item.name and item.price
ENDFOR
Display total_sum
Display cash_received
Display change
Display receipt footer

END
