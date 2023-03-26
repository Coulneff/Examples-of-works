<?php
$host='localhost';
$db = 'TelegramBot';
$username = 'TgBot';
$password = 'qwerty';

// Получаем логин и пароль из запроса
$login = $_POST['login'];
$password_user = $_POST['password'];

# Создаем соединение с базой PostgreSQL с указанными выше параметрами
$dbconn = pg_connect("host=$host port=5432 dbname=$db user=$username password=$password");
 
if (!$dbconn) {
die('Could not connect');
}
else {
#echo ("Connected to local DB");
# Выполняем запрос на создание таблицы testtable
 
# Сделаем запрос на получение списка созданных таблиц
$zapross = 'select * from Users where Users.Login='.$login.' and Users.Password='.$password_user;
 
$query ='SELECT "Users"."id","Users"."Login" FROM "Users" Where "Users"."Login"=$1 and "Users"."Password"=$2';
#$test =  'select * from "Users" Where "Users"."Login" = '.$login;
#$res = pg_query($dbconn, $query);
$res = pg_query_params($dbconn,$query,array($login,$password_user));

#$myrow = pg_fetch_all($res);
#$value == $myrow['Login'];
 

while ($row = pg_fetch_row($res)){
  $response = array('success' => true);
  $id_user = $row[0];
  setcookie("UserID",$id_user,strtotime("+1 days"));
  session_start();
  //echo session_id();
  $_SESSION['UserID'] = $id_user;
  //echo $_SESSION['UserID'];
}

if ($response == null)
{
  $response = array('denied' => false);
}


# Выведем полученные строки
}


// Отправляем ответ на клиент
header('Content-Type: application/json');
echo json_encode($response);


?>


