document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowUp') {
        move_up();
    } else if (event.key === 'ArrowDown') {
        move_down();
    } else if (event.key === 'ArrowLeft') {
        move_left();
    } else if (event.key === 'ArrowRight') {
        move_right();
    }
});
