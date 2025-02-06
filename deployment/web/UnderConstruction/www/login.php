<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type=text], input[type=password] {
            margin: 10px 0;
            padding: 10px;
            width: 200px;
            display: block;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type=submit] {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <form method="POST">
        <div>
            <label for="username">Username:</label>
            <input type="text" name="username" id="username">
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password">
        </div>
        <div>
            <input type="submit" value="Login">
        </div>
    </form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_REQUEST['username'];
    $password = $_REQUEST['password'];

    // Connection to the database (assumes localhost, root, no password)
    $conn = new mysqli("127.0.0.1", "root", "PasswordMomento!!!", "ctf_challenge");

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 

    // Vulnerable SQL query
    $sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Successful login
        echo "<p>Login successful! Welcome back, $username!</p>";
    } else {
        // Authentication failed
	    echo "<p>Login failed! Please try again.</p>";
	    echo $conn->error;
    }

    $conn->close();
}
?>

</body>
</html>
