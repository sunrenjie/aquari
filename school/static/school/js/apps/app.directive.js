(function() {
    'use strict';

    angular
        .module('school.apps.directives')
        .directive('app', app);

    function app() {
        var directive = {
            restrict: 'E',
            scope: {
                app: '='
            },
            templateUrl: '/static/school/templates/apps/app.html'
        };
        return directive;
    }
})();
