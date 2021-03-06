(function() {
    'use strict';
    angular
      .module('thinkster.authentication.services')
        .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    function Authentication($cookies, $http) {
        var Authentication = {
            register: register,
            login: login,
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate,
            logout: logout
        };
        return Authentication;

        function register(email, password, username) {
            return $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            }).then(registerSuccessFn, registerErrorFn);

            function registerSuccessFn(data, status, headers, config) {
                Authentication.login(username, password);
            }

            function registerErrorFn(data, status, headers, config) {
                console.error('Epic failure!');
            }

        }

        function login(username, password) {
            return $http.post('/api/v1/auth/login/', {
                username: username,
                password: password
            }).then(loginSuccessFn, loginErrorFn);
        }

        function loginSuccessFn(data, status, headers, config) {
            Authentication.setAuthenticatedAccount(data.data);
            window.location = '/';
        }

        function loginErrorFn(data, status, headers, config) {
            console.error('Epic failure:');
            console.error(data);
        }

        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }
            return JSON.parse($cookies.authenticatedAccount);
        }

        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }

        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }

        function unauthenticate() {
            delete $cookies.authenticatedAccount;
        }

        function logout() {
            return $http.post('/api/v1/auth/logout/')
                .then(logoutSuccessFn, logoutErrorFn);
        }

        function logoutSuccessFn(data, status, headers, config) {
            Authentication.unauthenticate();
            window.location = '/';
        }

        function logoutErrorFn(data, status, headers, config) {
            console.error('Epic failure!');
        }
    }
})();
