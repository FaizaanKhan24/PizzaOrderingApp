document.addEventListener('DOMContentLoaded',() => {
    document.querySelector('#placeOrder').onsubmit = () => {
        location.href = "place_order";

         return false
    }

    document.querySelectorAll("button.remove").forEach(button => {
        button.onclick = () => {            
            let itemId = parseInt(button.dataset.id);
            location.href = "remove/"+itemId;
        }
    });
});