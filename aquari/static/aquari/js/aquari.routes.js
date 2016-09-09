(function() {
    angular
        .module('aquari.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/aquari/templates/layout/index.html'
            })
            .otherwise('/');
    }
})();
