$(document).on('submit', '.form', function(e) {
     $.ajax({
        url: $(this).attr('action'),
        type: $(this).attr('method'),
        data: $(this).serialize(),
        success: function(html) {
        $(".form").clearForm();
        // $(".message").html(html);
        // alert('Спасибо за Ваш вопрос!');
        bootbox.alert({
          message: "<div class='alert' > Спасибо!</div>", 
          backdrop: true,
          buttonName: {
            'OK': {
                label: 'OK',
                className: 'btn'
            },
          }

        });
        }
    });
    e.preventDefault();
});
