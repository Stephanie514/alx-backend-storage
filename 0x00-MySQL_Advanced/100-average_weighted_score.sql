--SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
--that computes and store the average weighted score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    
    -- Calculating total weighted score and total weight
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;
    
    -- Calculating average weighted score
    DECLARE average_score DECIMAL(10, 2);
    IF total_weight > 0 THEN
        SET average_score = total_score / total_weight;
    ELSE
        SET average_score = 0;
    END IF;
    
    -- Updating users table with the average weighted score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //

DELIMITER ;
