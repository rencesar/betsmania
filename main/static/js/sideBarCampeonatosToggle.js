var trigger = $('.list-group-item'),
   isClosed = false;

  trigger.click(function () {
    toggle();
  });

  function toggle() {

    if (isClosed == true) {
      trigger.removeClass('is-open');
      trigger.addClass('is-closed');
      isClosed = false;
    } else {
      trigger.removeClass('is-closed');
      trigger.addClass('is-open');
      isClosed = true;
    }
}

$('[data-toggle="true"]').click(function () {
      $('.sidebar-campeonatos').toggleClass('toggled');
});
