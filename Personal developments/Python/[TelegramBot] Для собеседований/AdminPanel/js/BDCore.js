function login() {
    const login = document.getElementById('login').value;
    const password = document.getElementById('password').value;
    
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'php/Autho.php');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
        const response = JSON.parse(xhr.responseText);
        if (response.success) {
              window.open("Main.html","_self",false);
            //window.open("Main.html");
          // Пользователь успешно авторизован
          // Обновляем страницу или перенаправляем на другую страницу
        } else {
            console.log("Ошибка - неправильный логин/пароль");
          // Не удалось авторизоваться
          // Выводим сообщение об ошибке
        }
      }
    };
    xhr.send('login=' + encodeURIComponent(login) + '&password=' + encodeURIComponent(password));
  }

  function checkUser()
  {
    const name = "UserID";
    //const cookie = document.cookie;
    //console.log("checkUuser..");
    //var mycookie = document.cookie.replace(/(?:(?:^|.*;\s*)UserID\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    //console.log('UserID: '+mycookie);

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'php/cookieCheck.php');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
        const response = JSON.parse(xhr.responseText);
        if (response) {
          //console.log("no problem");
            //  window.open("Main.html","_self",false);
            //window.open("Main.html");
          // Пользователь успешно авторизован
          // Обновляем страницу или перенаправляем на другую страницу
        } else {
            console.log("Ошибка - неправильный логин/пароль");
            CookieSet("UserID","0");
            window.open("Index.html","_self","false");
          
        }
      }
      
    };
    xhr.send();
    //console.log(document.cookie);
  }

  function CookieSet(Param1,Param2)
  {
    const xhr1 = new XMLHttpRequest();
    console.log("!");
    xhr1.open('POST', 'php/cookieSet.php');
    xhr1.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr1.send('Parametr0='+encodeURIComponent(Param1)+'&Parametr1='+encodeURIComponent(Param2));

    //xhr1.open('POST','php/Session/SessionMain.php');
    
    //window.open("Index.html","_self","false");
  }

  function SessionEnd(){
    const xhr1 = new XMLHttpRequest();
    console.log("!");
    xhr1.open('POST', 'php/Session/SessionExit.php');
    xhr1.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr1.send();
    window.open("Index.html","_self","false");
  }

  function AddTable(tableName,tableColons){
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'php/TableUpdate.php');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
        const response = (xhr.responseText);
        if (response) {
          document.getElementById("ID_Zayvku").innerHTML = response;
        } 
      }
      
    };
    xhr.send('IdTable=' + encodeURIComponent("1"));

    
    //document.getElementById("ID_Zayvku").innerHTML = zaprTest;
    //console.log(tableColons);
    console.log("1");
  }


 