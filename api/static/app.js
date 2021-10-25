$(function() {

      $('.addForm').on('submit', function(event) {
        event.preventDefault();

        $.ajax({
          'url': 'add',
          'data': $('.addForm').serialize(),
          'method': 'POST'
        })
           .done(function(data) {
              $('#tasks').html(data);
           });

        return false;
      });

      $('#tasks').on('click', '.remove-btn', function(event) {
        event.preventDefault();

        var form = $(event.target).closest('form');
        $.ajax({
          'url': form.attr('action'),
          'data': form.serialize(),
          'method': 'POST'
        })
           .done(function(data) {
              form.closest('.card').remove();
           });

        return false;
      });

      $('#tasks').on('click', '.edit-btn', function(event) {
        event.preventDefault();
        var $card = $(event.target).closest('.card');
        var form = $(event.target).closest('form');

        $.ajax({
          'url': form.attr('action'),
          'data': form.serialize(),
          'method': 'POST'
        })
           .done(function(data) {
              $card.html(data);
              var $editForm = $card.find('form');

              $editForm.on('submit', function(event) {
                event.preventDefault();

                $.ajax({
                  'url': $editForm.attr('action'),
                  'data': $editForm.serialize(),
                  'method': 'POST'
                })
                   .done(function(data) {
                      $('#tasks').html(data);
                   });

                return false;
              });
           });

        return false;
      });
});