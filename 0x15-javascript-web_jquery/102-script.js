$(document).ready(function () {
  $('input#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=';
    const language = $('input#language_code').val();
    const fullUrl = url + language;
    $.get(fullUrl, function (data) {
      $('div#hello').text(data.hello);
    });
  });
});
