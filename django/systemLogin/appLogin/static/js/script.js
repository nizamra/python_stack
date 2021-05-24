document.getElementById("myForm").addEventListener("submit", checkPasswd);
let thisPass=document.getElementById('password').value;


function checkPasswd(thisPass) {
    if (thisPass.length < 8){
        return alert("Short Password MUST be longer than 8 charecters")
    }
    if(thisPass.match(/[0-9]+/) != null){
        return alert("Password MUST contain a number")
    }
    if(thisPass.match(/[a-z]+/) != null){
        return alert("Password MUST contain a LOWERcase letter")
    }
    if(thisPass.match(/[A-Z]+/) != null){
        return alert("Password MUST contain an UPPERcase letter")
    }
    if(thisPass.match(/[-!@#$%^&*()+]+/) != null){
        return alert("Password MUST contain a special character")
    }
    return True;
}