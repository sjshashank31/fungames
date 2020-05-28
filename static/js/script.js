function circle(el) {
    $(el).circleProgress({ fill: { color: '#ff5c5c' } }).on('circle-animation-progress', function (event, progress, stepvalue) {
        $(this).find('strong').text(String(stepvalue.toFixed(2)).substr(2) + '%');
    });
};
circle('.round');
