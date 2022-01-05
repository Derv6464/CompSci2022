var open = 0

function hamToX(x) {
    x.classList.toggle("change");
    console.log(open)
    if (open%2==0){
        openNav()
    } else{
        closeNav()
    }
    open = open +1
}

function openNav(){
    console.log("open nav")
    document.getElementById("myNav").style.width = "50%";
}

function closeNav(){
    console.log("close nav")
    document.getElementById("myNav").style.width = "0%";
}