function minimumNumber(password) {
    if (password.length < 8){
        return alert("Short Password MUST be longer than 8 charecters")
    }
    if(password.match(/[0-9]+/) != null){
        return alert("Password MUST contain a number")
    }
    if(password.match(/[a-z]+/) != null){
        return alert("Password MUST contain a LOWERcase letter")
    }
    if(password.match(/[A-Z]+/) != null){
        return alert("Password MUST contain an UPPERcase letter")
    }
    if(password.match(/[-!@#$%^&*()+]+/) != null){
        return alert("Password MUST contain a special character")
    }
    return True;
}