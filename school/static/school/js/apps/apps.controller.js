(function() {
    'use strict';

    angular
        .module('school.apps.controllers')
        .controller('AppsController', AppsController);

    AppsController.$inject = ['$scope'];

    function AppsController($scope) {
        var vm = this;
        vm.columns = [];
        activate();

        function activate() {
            $scope.$watchCollection(function() { return $scope.apps; }, render);
            $scope.$watch(function() { return $(window).width(); }, render);
        }

        function calculateNumberOfColumns() {
            var width = $(window).width();
            if (width >= 1200) {
                return 4;
            } else if (width >= 992) {
                return 3;
            } else if (width >= 768) {
                return 2;
            } else {
                return 1;
            }
        }

        function approximateShortestColumn() {
            var scores = vm.columns.map(columnMapFn);
            return scores.indexOf(Math.min.apply(this, scores));
        }

        function columnMapFn(column) {
            var lengths = column.map(function (element) {
                return element.summary.length;
            });

            return lengths.reduce(sum, 0) * column.length;
        }

        function sum(m, n) {
            return m + n;
        }

        function render(current, original) {
            if (current !== original) {
                alert(current.length);
                vm.columns = [];

                for (var i = 0; i < calculateNumberOfColumns(); ++i) {
                    vm.columns.push([]);
                }

                for (var i = 0; i < current.length; ++i) {
                    var column = approximateShortestColumn();
                    vm.columns[column].push(current[i]);
                }
            }
            window.zzzax = vm.columns;
        }
    }
})();
