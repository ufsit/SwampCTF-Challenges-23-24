<?php
//ini_set('display_errors', 0);

function charToBraille($character){
	$host = 'db'; // The service name of the PostgreSQL container
	$db   = 'brailleDB'; // Your database name
	$user = 'dbuser'; // Your database user
	$pass = 'IdkItsAPassword123!#2'; // Your database password

	$dsn = "pgsql:host=$host;dbname=$db";
	$options = [
		PDO::ATTR_ERRMODE			=> PDO::ERRMODE_EXCEPTION,
		PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
		PDO::ATTR_EMULATE_PREPARES   => false,
	];

	try {
		$pdo = new PDO($dsn, $user, $pass, $options);
		
		// Fetch all rows from the "braille" table
		$sql = "SELECT braille_representation FROM braille WHERE character = '".$character."'";

		$results = $pdo->query($sql)->fetchAll(PDO::FETCH_ASSOC);
		if(isset($results[0])){
			return $results[0]['braille_representation'];
		}
		else{
			http_response_code(400);
			echo "ERROR: One or more characters not avialable in BrailleDB";
			exit;
		}
	} catch (\PDOException $e) {
		throw new \PDOException($e->getMessage(), (int)$e->getCode());
	}
}

if (isset($_POST["searchText"])){
	$response = "";
	$searchText = $_POST["searchText"];
	echo charToBraille($searchText);
}
?>
