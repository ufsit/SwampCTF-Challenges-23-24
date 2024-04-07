<?php
//ini_set('display_errors', 0);

function submitFeedback($feedback){
	$host = 'db'; // The service name of the PostgreSQL container
	$db   = 'brailleDB'; // Your database name
	$user = 'dbuser'; // Your database user
	$pass = 'IdkItsAPassword123!#2'; // Your database password

	$dsn = "pgsql:host=$host;dbname=$db;options='--client_encoding=UTF8'";
	$options = [
		PDO::ATTR_ERRMODE			=> PDO::ERRMODE_EXCEPTION,
		PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
		PDO::ATTR_EMULATE_PREPARES   => false,
	];

	try {
		$pdo = new PDO($dsn, $user, $pass, $options);
		
		// Fetch all rows from the "braille" table
		$sql = "INSERT INTO feedback (feedback) VALUES ('".$feedback."')";
		$pdo->query($sql);
	} catch (\PDOException $e) {
		throw new \PDOException($e->getMessage(), (int)$e->getCode());
	}
}

function brailleToChar($character){
	$host = 'db'; // The service name of the PostgreSQL container
	$db   = 'brailleDB'; // Your database name
	$user = 'dbuser'; // Your database user
	$pass = 'IdkItsAPassword123!#2'; // Your database password

	$dsn = "pgsql:host=$host;dbname=$db;options='--client_encoding=UTF8'";
	$options = [
		PDO::ATTR_ERRMODE			=> PDO::ERRMODE_EXCEPTION,
		PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
		PDO::ATTR_EMULATE_PREPARES   => false,
	];

	try {
		$pdo = new PDO($dsn, $user, $pass, $options);
		
		// Fetch all rows from the "braille" table
		$stmt = $pdo->prepare("SELECT character FROM braille WHERE braille_representation = :character");
		$stmt->bindParam(':character', $character, PDO::PARAM_STR);
		$stmt->execute();

		$results = $stmt->fetchAll(PDO::FETCH_ASSOC);
		if(isset($results[0])){
			return $results[0]['character'];
		}
		else{
			http_response_code(400);
			echo "ERROR: Please submit feedback in braille for our employees";
			exit;
		}
	} catch (\PDOException $e) {
		throw new \PDOException($e->getMessage(), (int)$e->getCode());
	}
}

if (isset($_POST["feedbackText"])){
	$feedback = "";
	$brailleFeedback = $_POST["feedbackText"];
	for ($i = 0; $i < mb_strlen($brailleFeedback, 'UTF-8'); $i++){
		$character = mb_substr($brailleFeedback, $i, 1, 'UTF-8');
		$feedback .= brailleToChar($character);
	}
	submitFeedback($feedback);
	echo "Feedback successfully submitted!";
}
?>
