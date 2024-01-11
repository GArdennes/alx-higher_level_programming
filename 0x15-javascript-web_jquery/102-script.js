$(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val(); // Use val() to get the input value
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;

    fetch(url)
      .then(response => response.json()) // Use response.json() to parse JSON
      .then(data => {
        $('DIV#hello').text(data.hello);
      });
  });
});
