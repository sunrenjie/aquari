(function() {
    'use strict';

    angular
        .module('aquari.layout.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope'];

    function NavbarController($scope) {
        var vm = this;
        vm.logout = logout;

        function logout() {
            alert('fun!')
        }
    }
})();
