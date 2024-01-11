$(function () {
  $('INPUT#btn_translate').click(translateHello);

  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if the pressed key is Enter (key code 13)
      translateHello();
    }
  });

  function translateHello () {
    const languageCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    fetch(url)
      .then(response => response.json())
      .then(data => {
        $('DIV#hello').text(data.hello);
      });
  }
});
