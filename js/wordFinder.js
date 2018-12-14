const URL = "https://sbimochan.pythonanywhere.com";
window.addEventListener('load', function () {
  function sendData(form) {
    var data = { letters: form.letters.value, size: form.size.value };
    return fetch(URL, {
      method: "POST",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json; charset=utf-8"
      },
      redirect: "follow",
      body: JSON.stringify(data)
    }).then(response => response.json())
  };

  var form = document.getElementById('wordFinderForm');
  form.addEventListener('submit', function (event) {
    event.preventDefault();
    document.getElementById('heading4').innerHTML = "Loading...";
    sendData(form).then(data => {
      document.getElementById('heading4').innerHTML = data.msg;
      document.getElementById('resultArea').innerHTML = data.result;
    }).catch(err => document.getElementById('heading4').innerHTML = "Sorry, something went wrong. " + err)
  });
});