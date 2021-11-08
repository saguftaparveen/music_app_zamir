function myFunc(){
    let name=document.getElementById("name").value
    let pass=document.getElementById("password").value
    
   

    if(name==pass){
        document.getElementById("message").style.display = "block"
        document.getElementById("formpage").style.display = "none"
        
    //     document.getElementsByTagName("form").innerHTML="yaaahooo you are in"
    //    window.location="./premium.html"
        location.href="./premium.html"    
    }
    else{
        alert("use right password")
        return false
    }
    return false
}

function home(){
    location.href="http://127.0.0.1:8000/"
}