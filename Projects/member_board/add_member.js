function validateForm() {
    let name = document.forms["myForm"]["inputName"].value;
    let role = document.forms["myForm"]["inputRole"].value;
    let email = document.forms["myForm"]["inputEmail"].value;
    if (name == "") {
      alert("Name must be filled out");
      return false;
    }
    else if (role == "") {
        alert("Role must be filled out");
        return false;
    }
    else if (email == "")  {
        alert ("email must be filled out");
        return false;
    }
}