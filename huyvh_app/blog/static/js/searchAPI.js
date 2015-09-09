var app = angular.module("MyBlog", []);
app.controller("SearchCtrl", function($scope, $http) {
   $scope.url = 'http://localhost:8000/searchblog/'; // The url of our search
	// The function that will be executed on button click (ng-click="search()")
	$scope.search = function() {
		 initData($scope, $http);
	};
	initData($scope, $http);
});
function initData(scope, http) {
	if (scope.keywords == undefined) {
  	 		scope.keywords ='';
  		}
		http.get(scope.url+'?keywords='+scope.keywords).
		success( function( data, status ) {
			scope.Arrhuyvh = data;
		}).		
		error( function(data, status ) {
			//$scope.data = data || "Request failed";
			//$scope.status = status;			
			"Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header 
		});

}
/*
This directive allows us to pass a function in on an enter key to do what we want.
 */
app.directive('ngEnter', function () {
    return function (scope, element, attrs) {
        element.bind("keydown keypress", function (event) {
            if(event.which === 13) {
                scope.$apply(function (){
                    scope.$eval(attrs.ngEnter);
                }); 
                event.preventDefault();
            }
        });
    };
})
