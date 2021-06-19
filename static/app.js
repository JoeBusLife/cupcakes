const BASE_URL = "http://127.0.0.1:8050";
const $cupcakeForm = $("#cupcake-form");
const $cupcakeFormReset = $("#cupcake-form-reset");
const $cupcakes = $("#cupcakes");

class Cupcake {
	constructor(flavor, size, rating, image){
		this.flavor = flavor;
		this.size = size;
		this.rating = rating;
		this.image = image;
	} 

	static async fetchAllCupcakes(){
		let cupcakes = await axios.get(BASE_URL + "/api/cupcakes")
		return cupcakes.data.cupcakes;
	}

	static createCupcakes(cupcakes){
		$cupcakes.empty();
		for (const cupcake of cupcakes){
			$cupcakes.append(
				`<li>
					<div class="cupcakes-div" data-id="${cupcake.id}">
						<span class="">Flavor: ${cupcake.flavor}</span>
						<span class="">Size: ${cupcake.size}</span>
						<span class="">Rating: ${cupcake.rating}</span>
						<img class="cupcake-photo" src="${cupcake.image}" alt="${cupcake.flavor} cupcake">
					</div>
				</li>`)
		}
	}

	async sendNewCupcake(){
		let res = await axios.post(BASE_URL + "/api/cupcakes", {flavor: this.flavor, size: this.size, rating: this.rating, image: this.image});
	}

}

async function showAllCupcakes(){
	Cupcake.createCupcakes(await Cupcake.fetchAllCupcakes())
}

async function handleFormSubmit(evt){
	evt.preventDefault();
	const newCupcake = new Cupcake($("#flavor").val(), $("#size").val(), parseFloat($("#rating").val()), $("#image").val())
	await newCupcake.sendNewCupcake()

	Cupcake.createCupcakes(await Cupcake.fetchAllCupcakes())
	evt.target.reset();
}

$cupcakeForm.on("submit", handleFormSubmit);

$cupcakeFormReset.on("click", function(evt){
	evt.target.parentElement.reset();
});

$(window).on("load", showAllCupcakes);