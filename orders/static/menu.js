document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#regularsubmit').onsubmit = ()=>{
        let size = document.querySelector('#sizeValue').value;
        let toppings = document.querySelector('#toppings').options;

        let outputString = GetOutputString(toppings);
        outputString = "rpizza&&" + outputString;
        outputList = outputString.split("?");
        let itemTypeString = outputList[0];
        let itemId = parseInt(outputList[1]);

        location.href = "add/"+itemTypeString+"/"+size+"/"+itemId;

        return false;
    };

    document.querySelector("#siciliansubmit").onsubmit = ()=>{
        let size = document.querySelector("#SicilainSizeValue").value;
        let toppings = document.querySelector("#SicilainToppings").options;

        let outputString = GetOutputString(toppings);
        outputString = "spizza&&" + outputString;
        outputList = outputString.split("?");
        let itemTypeString = outputList[0];
        let itemId = parseInt(outputList[1]);

        location.href = "add/"+itemTypeString+"/"+size+"/"+itemId;

        return false;
    };
});
function GetOutputString(toppings){
    let toppingsList = [];
    for(let option of toppings){
        if(option.selected){
            toppingsList.push(option.value);
        }
    }
    let listLength = toppingsList.length;
    let pizzaType = "";
    let id="";
    if(listLength == 0){
        pizzaType = "Cheese Pizza";
        id="1";
    }
    else if(listLength>3){
        pizzaType = "Special Pizza";
        id="5";
    }
    else{
        pizzaType = listLength + " Topping Pizza"; 
        id=(listLength+1).toString();
    }
    let outputString = toppingsList.join("&&")+"?"+id;

    return outputString;
}