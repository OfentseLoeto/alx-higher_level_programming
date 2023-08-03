const $ = window.$;
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    Type: 'GET',
    success: function (data) {
      $('#character').text(data.name);
    },
    error: function (xhr, status, error) {
      console.error('Error fetching name:', error);
    }
  });
});
