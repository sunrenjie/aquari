(function() {
    'use strict';

    angular
        .module('aquari.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'Apps', 'Snackbar'];

    function IndexController($scope, Apps, Snackbar) {
        var vm = this;

        vm.apps = [];

        activate();

        function activate() {
            Apps.all().then(successFn, errorFn);
            $scope.$on('app.created', function(event, app) {
                vm.apps.unshift(app);
            });
            $scope.$on('app.created.error', function() {
                vm.apps.shift();
            });
        }

        function successFn(data, status, headers, config) {
            vm.apps = data.data;
        }

        function errorFn(data, status, headers, config) {
            Snackbar.error(data.error);
        }
    }
})();
