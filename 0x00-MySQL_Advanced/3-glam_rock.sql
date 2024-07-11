-- Buy buy buy
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON mydatabase.orders FOR EACH ROW 
BEGIN
    DECLARE item_id INT;
    DECLARE order_quantity INT;
    
    SELECT NEW.item_id, NEW.quantity INTO item_id, order_quantity;

    UPDATE mydatabase.items
    SET quantity = quantity - order_quantity
    WHERE id = item_id;
END //
DELIMITER ;
