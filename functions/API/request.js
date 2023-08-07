function main(params) {
    params = params.review;
    
	return {doc:{
	    name: params.name,
	    id:params.id,
        dealership: params.dealership,
        review: params.review,
        purchase: params.purchase,
        purchase_date: params.purchase_date,
        car_make: params.car_make,
        car_model: params.car_model,
        car_year: params.car_year
	} };
}