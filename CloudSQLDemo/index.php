<html>
<head><title>Welcome to my Cloud SQL Demo</title></head>
<body>
<h1>Welcome Everyone</h1>
<?php
 $dbserver = "ip-of-cloud-sql";
 $dbuser = "user-of-cloud-sql";
 $dbpassword = "pwd";
$conn = new mysqli($dbserver, $dbuser, $dbpassword);
if (mysqli_connect_error()) {
       echo ("Database connection failed: " . mysqli_connect_error());
} else {
       echo ("Database connection succeeded.");
}
?>
</body></html>