function Func(){
    let name=window.prompt("Type your Name:");
    let age=window.prompt("Type your Age:");
    if(age>=18){
        window.alert("You are free to go "+name+" you are above 18 years old");
    }
    else if(age<18){
        window.alert("You must be over 18 years old "+name);
    }
}