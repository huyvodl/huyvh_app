function callWS($scope, $http) {
    $http.get('http://localhost:8000/ws/?format=json').
        success(function(data) {
        	//alert(data);
        	//var carsFromServer = JSON.parse(data);
           // $scope.cars = carsFromServer.allCars;
            $scope.results = data;
        });
}