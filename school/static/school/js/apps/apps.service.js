(function() {
    'use strict';

    angular
        .module('school.apps.services')
        .factory('Apps', Apps);

    Apps.$inject = ['$http'];

    function Apps($http) {
        var Posts = {
            all: all
        };
        return Posts;

        function all() {
            return $http.get('/api/v1/apps/');
        }
    }
})();
