<?php
// Получаем логин и пароль из запроса
$Parametr0 = $_POST['Parametr0'];
$Parametr1 = $_POST['Parametr1'];
echo $Parametr0;
  #$response = array('success' => true);
setcookie($Parametr0,$Parametr1);

?>