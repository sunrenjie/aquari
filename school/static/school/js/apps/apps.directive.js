(function() {
    'use strict';

    angular
        .module('school.apps.directives')
        .directive('apps', apps);

    function apps() {
        var directive = {
            controller: 'AppsController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                apps: '='
            },
            templateUrl: '/static/school/templates/apps/apps.html'
        };
        return directive;
    }
})();
