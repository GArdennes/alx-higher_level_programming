window.onload = function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => response.text())
    .then(data => {
      $('DIV#hello').text(data);
    });
};
