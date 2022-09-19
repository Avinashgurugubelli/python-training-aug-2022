# 02. Post office 

- A post office wants to automate the process of allocation of letters to different postmen based on their allocated area. Write a python program to implement the class diagram given below.

![alt](./resources/02_post_office_assignment.png)

## Class description

### Letter class:

Initialize static variable counter to 1
Auto-generate attribute, letter_id starting from 1 in the constructor
PostMan class:

Initialize static variable counter to 100
Auto-generate attribute, postman_id starting from 101 prefixed by “P” in the constructor
post_list_to_deliver: List of letter objects to be delivered by the postman

### PostOffice class:

- **area_list:** List of names of areas under the post office
- **postmen_list:** List of postman objects working in the post office. There is one to one correspondence between the two lists – which means postman at index position 0 delivers letters in the area at index position 0 of area_list
- **validate_letter(letter):** Accept the letter and validate its receiver area. If letter.receiver_area is present in area_list, return the index position of that area in area_list. Else return -1
- **allocate_posts(letter_list):** Allocate letters in the letter_list to the appropriate postman
  - For every letter in letter_list
        - Validate letter.receiver_area
        - If valid, append the letter to the corresponding postman's post_list_to_deliver
        - Else, add it to an invalid letter list
  - Return invalid letter list
Perform case sensitive comparison.
Create objects of Letter class, PostMan class and PostOffice class, invoke appropriate methods and test your program.

## 03. ABC Mart online services

- ABC Mart has made its service online for few of the products available in the mart by providing additional online discount and with a feature of shipping the order to the customers through courier. The process of calculation of the order price and shipping the order request to customer and providing them tracking id process has to be automated.
- The class design for the same is given below.

## Notes

- Do not include any extra instance/static variables instance/static methods in the given classes

- Case sensitive comparison is required to be done wherever applicable

- Do not change any value or case of the given variables

- Read notes and examples carefully for better understanding of the logic

![alt](./resources/03_1..png)

## Order class

### generate_tracking_id()

- This method auto generates the tracking_id (String) for each order successfully shipped.
- The tracking_id should be auto-generated from "TR1000" followed by "TR1001", "TR1002" and so on. I.e. first tracking_id should be "TR1000", the second should be "TR1001" and so on
- Use static variable counter (integer) appropriately for auto-generation logic


## Mart class

- There are three static lists in this class. They are –
  - item_name_list: has the name of each item (string) available in the Mart
  - item_price_list: has the unit price (integer) of each item available in the Mart
  - item_quantity_list: has current quantity of each item (integer) available in the Mart.

- The initial values of these lists are as below –

![alt](resources/03_2.png)

  These lists have one to one correspondence. I.e. the unit price of "Bouquet" is Rs. 150/- and there are 30 pieces (quantity) available in the Mart

Note: Mart class is supplied. No need to code these lists

## OnlineMart class

## check_item_availability()

- This method validates the **item_name** (string) of the order. This method also validates if the Mart has sufficient **quantity_required** (integer) in **item_quantity_list** for the given **item_name** of the order.
- Check if the item_name of the order is available in the **item_name_list** of the Mart class
- If not available, return -1
- Otherwise, check if sufficient **quantity_required** is available in item_quantity_list for the order.
- If not available, return -1
- Otherwise, Update the **item_quantity_list** of **Mart** class by deducting the **quantity_required** from existing value
- Return **quantity_required** for the order.

**Example 1:** If item_name is "Bouquet", quantity_required is 20 and item_quantity_list is [10, 20, 30, 40], this method updates the item_quantity_list as [10, 20, 10, 40] and returns 20.

**Example 2:** If item_name is "Blanket", quantity_required is 20 and item_quantity_list is [10, 20, 30, 40], this method returns -1 and the item_quantity_list remains same.

**Example 3:** If item_name is "Bouquet", quantity_required is 31 and item_quantity_list is [10, 20, 30, 40], this method -1 false and the item_quantity_list remains same.

## find_price_per_item(item name)

- This is an overridden method which takes item name (string) as an input parameter and returns the price per item (float) as per the logic below –
- Invoke the find_price_per_item() method of the Mart class by passing item name to get initial price per item.
- Check if initial price per item is -1
- If so, set the value of price per item to -1
Otherwise, invoke the calculate_online_discount() method to set online_discount_percentage
- Check if online_discount_percentage is -1
- If so, set the value of price per item to -1
- Otherwise,
  - Calculate discount on initial price per item using online_discount_percentage
  - Calculate the price per item by deducting discount calculated in the above step from initial price per item.
- Return price per item.

**Example 1:** If item name requested is "Bouquet" and payment_mode is provided as "Prepaid", the price per item is Rs. 380.00

**Example 2:** If item name requested is "Blanket" and payment_mode is provided as "Prepaid", the price per item is -1

**ship_order():**

- This method calculates the order_price of order.

- Invoke check_item_availability() method to get quantity

- Invoke find_price_per_item() method of OnlineMart class by passing item_name of order to get price per item

- If either quantity or price per item is -1, set order_price to -1 and tracking_id to "NA"

- Otherwise, Calculate and set order_price of order as the product of quantity and price per item

- Invoke generate_tracking_id() method of Order class to generate tracking_id

**Example 1:** For an order where item_name requested is "Bouquet", quantity_required is 20 and payment_mode is 'Prepaid', the order_price would be Rs. 1140.00 and tracking_id returned would be "TR1000".

**Example 2:** For an order where item_name requested is "Blanket", quantity_required is 20 and payment_mode is 'Prepaid', the order_price would be -1 and tracking_id returned would be "NA".

 
 