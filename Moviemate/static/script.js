$(function() {
    // Form validation
    $('#searchForm').on('submit', function(e) {
        var title = $('#title').val().trim();
        if (!title) {
            alert('Please enter a movie title.');
            e.preventDefault();
        }
    });

    // Add to watchlist
    $('.add-watchlist').on('click', function() {
        var btn = $(this);
        var movie = {
            title: btn.data('title'),
            id: btn.data('id'),
            poster: btn.data('poster'),
            rating: btn.data('rating'),
            year: btn.data('year'),
            summary: btn.data('summary')
        };
        $.ajax({
            url: '/add_to_watchlist',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(movie),
            success: function(res) {
                if (res.success) {
                    btn.addClass('added').text('Added!');
                } else {
                    alert(res.message);
                }
            }
        });
    });
});
