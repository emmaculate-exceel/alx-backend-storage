-- Buy buy buy

DELIMITER $$
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW BEGIN
  DECLARE new_quantity INT;

  SELECT quantity INTO new_quantity FROM items WHERE item_id = NEW.item_id;

  IF new_quantity >= NEW.quantity THEN
    UPDATE items SET quantity = quantity - NEW.quantity WHERE item_id = NEW.item_id;
  ELSE
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient stock for item';
  END IF;
END $$

DELIMITER ;
