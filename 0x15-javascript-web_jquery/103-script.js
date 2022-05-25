$(document).ready(function () {
  $('input#btn_translate').click(function () {
    fetchLanguage();
  });
  $(document).keypress(function (event) {
    if ($('input#language_code').is(':focus') && event.keyCode === 13) {
      fetchLanguage();
    }
  });
});

const fetchLanguage = function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  const language = $('input#language_code').val();
  const fullUrl = url + language;
  $.get(fullUrl, function (data) {
    $('div#hello').text(data.hello);
  });
};
