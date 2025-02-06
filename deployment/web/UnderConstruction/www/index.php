<?php
ini_set('display_errors', 0);
if (isset($_GET['page'])) {
    include("/var/www/html/".$_GET['page']);
} else {
    header('HTTP/1.1 301 Moved Permenently');
    header('Location: /?page=under_construction.php');
}
?>
