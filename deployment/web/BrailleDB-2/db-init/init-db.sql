-- Create the "braille" table
CREATE TABLE IF NOT EXISTS braille (
    id SERIAL PRIMARY KEY,
    character CHAR(1),
    braille_representation VARCHAR(255)
);

-- Feedback table
CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    feedback TEXT
);
CREATE OR REPLACE FUNCTION limit_rows() RETURNS TRIGGER AS $$
BEGIN
	IF (SELECT COUNT(*) FROM feedback) > 10 THEN
		DELETE FROM feedback WHERE id > 5;
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_row_limit
AFTER INSERT ON feedback
FOR EACH ROW
EXECUTE FUNCTION limit_rows();

-- Create the "flag" table
CREATE TABLE IF NOT EXISTS flag (
    id SERIAL PRIMARY KEY,
    flag TEXT
);

-- Insert an example entry into the "flag" table (Update this with your actual flag)
INSERT INTO flag (flag) VALUES ('swampCTF{S33ing_0utput_1s_0v3rrat3d}');

-- Note: You can manually insert entries into the "braille" table as needed
-- Example:
-- INSERT INTO braille (character, braille_representation) VALUES ('a', '⠸⠁');
INSERT INTO braille (character, braille_representation) VALUES (' ', '⠀');
INSERT INTO braille (character, braille_representation) VALUES ('A', '⠁');
INSERT INTO braille (character, braille_representation) VALUES ('1', '⠂');
INSERT INTO braille (character, braille_representation) VALUES ('B', '⠃');
INSERT INTO braille (character, braille_representation) VALUES ('''', '⠄');
INSERT INTO braille (character, braille_representation) VALUES ('K', '⠅');
INSERT INTO braille (character, braille_representation) VALUES ('2', '⠆');
INSERT INTO braille (character, braille_representation) VALUES ('L', '⠇');
INSERT INTO braille (character, braille_representation) VALUES ('@', '⠈');
INSERT INTO braille (character, braille_representation) VALUES ('C', '⠉');
INSERT INTO braille (character, braille_representation) VALUES ('I', '⠊');
INSERT INTO braille (character, braille_representation) VALUES ('F', '⠋');
INSERT INTO braille (character, braille_representation) VALUES ('/', '⠌');
INSERT INTO braille (character, braille_representation) VALUES ('M', '⠍');
INSERT INTO braille (character, braille_representation) VALUES ('S', '⠎');
INSERT INTO braille (character, braille_representation) VALUES ('P', '⠏');
INSERT INTO braille (character, braille_representation) VALUES ('"', '⠐');
INSERT INTO braille (character, braille_representation) VALUES ('E', '⠑');
INSERT INTO braille (character, braille_representation) VALUES ('3', '⠒');
INSERT INTO braille (character, braille_representation) VALUES ('H', '⠓');
INSERT INTO braille (character, braille_representation) VALUES ('9', '⠔');
INSERT INTO braille (character, braille_representation) VALUES ('O', '⠕');
INSERT INTO braille (character, braille_representation) VALUES ('6', '⠖');
INSERT INTO braille (character, braille_representation) VALUES ('R', '⠗');
INSERT INTO braille (character, braille_representation) VALUES ('^', '⠘');
INSERT INTO braille (character, braille_representation) VALUES ('D', '⠙');
INSERT INTO braille (character, braille_representation) VALUES ('J', '⠚');
INSERT INTO braille (character, braille_representation) VALUES ('G', '⠛');
INSERT INTO braille (character, braille_representation) VALUES ('>', '⠜');
INSERT INTO braille (character, braille_representation) VALUES ('N', '⠝');
INSERT INTO braille (character, braille_representation) VALUES ('T', '⠞');
INSERT INTO braille (character, braille_representation) VALUES ('Q', '⠟');
INSERT INTO braille (character, braille_representation) VALUES (',', '⠠');
INSERT INTO braille (character, braille_representation) VALUES ('*', '⠡');
INSERT INTO braille (character, braille_representation) VALUES ('5', '⠢');
INSERT INTO braille (character, braille_representation) VALUES ('<', '⠣');
INSERT INTO braille (character, braille_representation) VALUES ('-', '⠤');
INSERT INTO braille (character, braille_representation) VALUES ('U', '⠥');
INSERT INTO braille (character, braille_representation) VALUES ('8', '⠦');
INSERT INTO braille (character, braille_representation) VALUES ('V', '⠧');
INSERT INTO braille (character, braille_representation) VALUES ('.', '⠨');
INSERT INTO braille (character, braille_representation) VALUES ('%', '⠩');
INSERT INTO braille (character, braille_representation) VALUES ('[', '⠪');
INSERT INTO braille (character, braille_representation) VALUES ('$', '⠫');
INSERT INTO braille (character, braille_representation) VALUES ('+', '⠬');
INSERT INTO braille (character, braille_representation) VALUES ('X', '⠭');
INSERT INTO braille (character, braille_representation) VALUES ('!', '⠮');
INSERT INTO braille (character, braille_representation) VALUES ('&', '⠯');
INSERT INTO braille (character, braille_representation) VALUES (';', '⠰');
INSERT INTO braille (character, braille_representation) VALUES (':', '⠱');
INSERT INTO braille (character, braille_representation) VALUES ('4', '⠲');
INSERT INTO braille (character, braille_representation) VALUES ('\', '⠳');
INSERT INTO braille (character, braille_representation) VALUES ('0', '⠴');
INSERT INTO braille (character, braille_representation) VALUES ('Z', '⠵');
INSERT INTO braille (character, braille_representation) VALUES ('7', '⠶');
INSERT INTO braille (character, braille_representation) VALUES ('(', '⠷');
INSERT INTO braille (character, braille_representation) VALUES ('_', '⠸');
INSERT INTO braille (character, braille_representation) VALUES ('?', '⠹');
INSERT INTO braille (character, braille_representation) VALUES ('W', '⠺');
INSERT INTO braille (character, braille_representation) VALUES (']', '⠻');
INSERT INTO braille (character, braille_representation) VALUES ('#', '⠼');
INSERT INTO braille (character, braille_representation) VALUES ('Y', '⠽');
INSERT INTO braille (character, braille_representation) VALUES (')', '⠾');
INSERT INTO braille (character, braille_representation) VALUES ('=', '⠿');

