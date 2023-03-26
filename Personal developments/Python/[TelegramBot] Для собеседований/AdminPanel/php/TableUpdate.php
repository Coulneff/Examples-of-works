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
#$zapross = 'select * from Users where Users.Login='.$login.' and Users.Password='.$password_user;
 
$query ='SELECT "Zayvku"."id","Zayvku"."SotrF","Zayvku"."SotrN","Zayvku"."SotrO","Zayvku"."DateBitr","Zayvku"."Dolznost","Zayvku"."Status","Dolznost"."Name","StatusZayvku"."name" FROM "Zayvku"'.
' LEFT JOIN "Dolznost" on "Dolznost"."id" = "Zayvku"."Dolznost"'.
' LEFT JOIN "StatusZayvku" on "StatusZayvku"."id" = "Zayvku"."Status"';
#$test =  'select * from "Users" Where "Users"."Login" = '.$login;
$res = pg_query($dbconn, $query);
#$res = pg_query_params($dbconn,$query,array($login,$password_user));

#$myrow = pg_fetch_all($res);
#$value == $myrow['Login'];
 
$response="";
while ($row = pg_fetch_row($res)){
  $response = $response . "<tr><td>".$row[0]."</td><td>".($row[1])."</td><td>".($row[2])."</td><td>".$row[3]."</td><td>".$row[4]."</td><td>".$row[7]."</td><td>".$row[8]."</td><td><button onclick='OpenZauyvku(".$row[0].")'>Открыть</button></td></tr>";
}
 

# Выведем полученные строки
}


// Отправляем ответ на клиент
header('Content-Type: application/json');
echo  ($response);

function utf8_urldecode($str) {
  $str = preg_replace("/%u([0-9a-f]{3,4})/i","&#x\\1;",urldecode($str));
  return html_entity_decode($str,null,'UTF-8');;
}
?>