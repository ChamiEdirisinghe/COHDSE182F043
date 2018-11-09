<html>
<head>
<title>User_Login</title>
</head>

<body>
<form id="form1" name="form1" method="post" action="#">

<center>
<label for="lbl1">username</label>   <input type="text" name="username" id="textfield1"><br/><br/>
<label for="lbl2">Password</label>   <input type="password" name="password" id="textfield2"><br/><br/>
<input type="submit" value="login">
</center>

</form>
</body>
</html>

<?php
session_start();
if(isset($_POST["username"]))
{
$user =$_POST["username"];
$pwd =$_POST["password"];
if($user=="admin" && $pwd=="12345")
  {
	
	header("Location:welcome.php");
	$_SESSION['FINAL']=time();
	
  }
}
?>