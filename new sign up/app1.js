$(document).ready(function() {

  $('#log-in-button').on('click', function() {
    $('#log-in-button').addClass('active');
    $('#sign-up-button').removeClass('active');
    $('#sign-up-form').css('display', 'none');
    $('#log-in-form').css('display', 'block');
  });

  $('#sign-up-button').on('click', function() {
    $('#log-in-button').removeClass('active');
    $('#sign-up-button').addClass('active');
    $('#sign-up-form').css('display', 'block');
    $('#log-in-form').css('display', 'none');
  });
})