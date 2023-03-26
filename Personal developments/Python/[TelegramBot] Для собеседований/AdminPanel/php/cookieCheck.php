<?php
//echo $_SESSION['UserID'];
session_start();
if ($_SESSION['UserID'] <> null)
{
    $response = true;
}
else
$response = false;
 
  #$response = array('success' => true);
  #setcookie("UserID",$id_user);
 

 #echo $response;
  #$response = array('denied' => false);
 

// Отправляем ответ на клиент
header('Content-Type: application/json');
echo json_encode($response);
?>