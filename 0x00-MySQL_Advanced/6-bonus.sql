-- sql script that creates addBonus procedures

DELIMITER $$

CREATE PROCEDURE AddBonus(IN p_user_id INT, IN p_project_name VARCHAR(255), IN p_score DECIMAL(10,2))
BEGIN
  DECLARE p_project_id INT;

  IF NOT EXISTS (SELECT 1 FROM users WHERE id = p_user_id) THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'User not found';
  END IF;

  SELECT id INTO p_project_id FROM projects WHERE name = p_project_name;
  IF NOT FOUND THEN
    INSERT INTO projects (name) VALUES (p_project_name);
    SELECT LAST_INSERT_ID() INTO p_project_id;
  END IF;

  INSERT INTO corrections (user_id, project_id, score) VALUES (p_user_id, p_project_id, p_score);
END $$

DELIMITER ;
