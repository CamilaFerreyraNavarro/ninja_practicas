odoo.define('ninja_quiz.ninja_chart', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.QuizPodiumChart = publicWidget.Widget.extend({
        selector: '#podium',
        start: function () {
            if (typeof Chart === 'undefined') {
                console.error("Chart.js no está cargado");
                return;
            }

            const ctx = this.el;
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: playersData.labels,
                    datasets: [{
                        label: 'Puntos',
                        data: playersData.scores,
                        backgroundColor: ['#FFD700', '#C0C0C0', '#CD7F32', '#4caf50', '#2196f3', '#ff9800']
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    plugins: {
                        legend: { display: false },
                        title: {
                            display: true,
                            text: 'Podio de jugadores'
                        }
                    }
                }
            });
        }
    });
});
