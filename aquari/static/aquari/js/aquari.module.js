(function() {
    'use strict';

    angular
        .module('aquari', [
            'aquari.config',
            'aquari.routes',
            'thinkster.authentication',
            'aquari.utils',
            'aquari.layout',
            'school'
        ]);

    angular.module('aquari.routes', ['ngRoute']);

    angular.module('aquari.config', []);

    angular.module('aquari').run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }
})();
