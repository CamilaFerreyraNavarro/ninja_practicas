odoo.define('ninja_quiz.timer', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.KahootTimer = publicWidget.Widget.extend({
        selector: '#kahoot-timer',
        start: function () {
            const timerElement = this.$el;
            let time = parseInt(timerElement.text());

            if (isNaN(time)) {
                console.warn("Temporizador no tiene valor numérico");
                return;
            }

            const interval = setInterval(() => {
                time--;
                timerElement.text(time);
                if (time <= 0) {
                    clearInterval(interval);
                    timerElement.text("¡Tiempo!");
                }
            }, 1000);
        },
    });
});
