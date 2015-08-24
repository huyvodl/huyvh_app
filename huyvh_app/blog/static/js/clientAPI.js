var app = angular.module("MyBlog", []);
app.controller("callWSCtl", function($scope, $http) {
  $http.defaults.headers.common["X-Custom-Header"] = "Angular.js";
  $http.get('http://localhost:8000/ws').
    success(function(data, status, headers, config) {
      console.log("success!");
      $scope.Arrhuyvh = data.results;
    }).
    error(function(data, status, headers, config) {
      console.log("failed!");
    });
});

