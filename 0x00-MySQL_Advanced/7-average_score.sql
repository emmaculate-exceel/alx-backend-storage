-- a script that stored the procedure of average users

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);

    -- Compute the average score
    SELECT AVG(score) INTO avg_score
    FROM scores
    WHERE user_id = user_id;

    -- Update or insert the average score into the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
    
    -- If the user has no scores, set average_score to NULL
    IF avg_score IS NULL THEN
        UPDATE users
        SET average_score = NULL
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;
