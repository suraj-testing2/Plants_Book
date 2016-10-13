'use strict';

goog.provide('grrUi.client.clientLoadGraphSerieDirective.ClientLoadGraphSerieDirective');

goog.scope(function() {



/**
 * Registers serie in the graph.
 *
 * @return {angular.Directive} Directive definition object.
 * @export
 */
grrUi.client.clientLoadGraphSerieDirective.ClientLoadGraphSerieDirective =
    function() {
      return {
        scope: {
          clientId: '=',
          metric: '@',
          rate: '@',
          label: '@'
        },
        restrict: 'E',
        require: '^grrTimeseriesGraph',
        link: function(scope, element, attrs, grrTimeseriesGrpahCtrl) {
          // Only register the graph when client id has a value.
          scope.$watch("::clientId", function() {
            if (angular.isUndefined(scope.clientId)) {
              return;
            }

            var options = {};
            if (scope.rate) {
              options['rate'] = scope.rate;
            }

            var path = 'clients/' + scope.clientId + '/load-stats/' +
                scope.metric;

            grrTimeseriesGrpahCtrl.addSerieDescriptor({
              label: scope.label,
              requestPath: path,
              requestOptions: options
            });
          });
        }
      };
    };


/**
 * Name of the directive as registered in Angular.
 *
 * @const
 * @export
 */
grrUi.client.clientLoadGraphSerieDirective.
    ClientLoadGraphSerieDirective.directive_name = 'grrClientLoadGraphSerie';


});  // goog.scope
