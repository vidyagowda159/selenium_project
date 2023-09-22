const display = function () {
    fname = document.querySelector("#firstname").value
    lname = document.querySelector("#lastname").value
    alert(`Hello ${fname}, ${lname}`)
    document.querySelector("#firstname").value = ""
    document.querySelector("#lastname").value = ""
}
document.querySelector("#submit").addEventListener("click", display)

document.querySelector("#delete").addEventListener("click", function () {
    if (window.confirm("Are You Sure You Want to Delete")) {
        document.querySelector(".label_alert").textContent = "You clicked Ok!!!"
    } else {
        document.querySelector(".label_alert").textContent = "You clicked Cancel !!!"
    }
})

const dbl = function () {
    document.querySelector("#double-click-message").textContent = "You double clicked"
}

window.onload = function () {
    var output = document.getElementsByClassName('price');
    setInterval(function () {
        output[0].innerHTML = Number((Math.random()).toFixed(5));
    }, 1000);


    setInterval(function () {
        output[1].innerHTML = Number((Math.random()).toFixed(5));
    }, 2000);

    setInterval(function () {
        output[2].innerHTML = Number((Math.random()).toFixed(5));
    }, 1000);

    setInterval(function () {
        output[3].innerHTML = Number((Math.random()).toFixed(5));
    }, 3000);
};